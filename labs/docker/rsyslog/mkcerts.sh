#!/bin/sh
# Lab certificate authority for the SA-05 relay path. Three host certificates
# whose CN is the container hostname, which is what x509/name authentication
# checks. Never reuse these outside the lab.
set -e
cd "$(dirname "$0")"
mkdir -p certs && cd certs
[ -f ca.key ] || openssl req -x509 -newkey rsa:2048 -nodes -days 365 \
    -subj "/CN=oscd-lab-ca" -keyout ca.key -out ca.pem 2>/dev/null
for h in src-01 relay-01 central-01; do
  [ -f "$h.pem" ] && continue
  openssl req -newkey rsa:2048 -nodes -subj "/CN=$h" \
      -keyout "$h.key" -out "$h.csr" 2>/dev/null
  printf "subjectAltName=DNS:%s\n" "$h" > "$h.ext"
  openssl x509 -req -in "$h.csr" -CA ca.pem -CAkey ca.key -CAcreateserial \
      -days 365 -extfile "$h.ext" -out "$h.pem" 2>/dev/null
  rm -f "$h.csr" "$h.ext"
done
chmod 644 ./*.key      # the containers run rsyslog as root; readable is enough
echo "certificates in $(pwd):"; ls -1
