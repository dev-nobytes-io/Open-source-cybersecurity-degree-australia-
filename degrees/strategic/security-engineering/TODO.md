# TODO — degrees/strategic/security-engineering/

**Major:** Security Engineering
**Degree:** Bachelor of Cybersecurity Strategy
**Year:** 3
**Units:** SE01–SE06

All units are currently **Planned**. No unit files have been authored yet.

---

## Files to Create

| File | Unit | Description |
|---|---|---|
| `SE01-secure-system-design.md` | SE01 | Secure SDLC, threat modelling, security requirements, secure defaults |
| `SE02-security-architecture.md` | SE02 | SABSA, Zero Trust (NIST SP 800-207), cloud security architecture |
| `SE03-identity-access-management.md` | SE03 | IAM design, PAM, federation, MFA, directory services |
| `SE04-detection-response-engineering.md` | SE04 | SIEM/SOAR design, automation pipelines, XDR architecture |
| `SE05-security-cloud-devsecops.md` | SE05 | IaC security, container security, CI/CD pipeline hardening |
| `SE06-capstone-architecture-design.md` | SE06 | Secure architecture for a defined environment (capstone) |

---

## Bloom's Taxonomy Requirements

Units SE01–SE05: **Levels 4–5** (analyse, evaluate, design)
Capstone SE06: **Levels 5–6** (create, design, evaluate, justify)

Example verbs: design, architect, evaluate, construct, justify, recommend, specify

---

## Framework Mapping Requirements

| Framework | Required |
|---|---|
| NIST SP 800-160 (Systems Security Engineering) | Yes — SE01, SE02 |
| NIST CSF 2.0 | Yes — throughout |
| SABSA (SCF) | Yes — SE02 architecture layers |
| Zero Trust (NIST SP 800-207) | Yes — SE02 |
| NIST SP 800-207 | Yes — SE02 |
| SFIA 9 (ARCH) | Yes — at least 2 units |
| NIST NICE DCWF | Yes — T-codes traceable to labs |
| ASD Essential Eight | Yes — SE01 secure defaults, SE05 DevSecOps |

---

## Lab Requirements

At least 8 labs total. Tools should be free or open-source where possible.

### Required Labs Across the Major

| Unit | Lab Ideas |
|---|---|
| SE01 | Lab: Create a threat model for a fictional web application using Microsoft Threat Modelling Tool |
| SE01 | Lab: Audit a set of system design decisions against NIST SP 800-160 principles; produce a gap analysis |
| SE02 | Lab: Map a fictional organisation's architecture to the SABSA layers |
| SE02 | Lab: Design a Zero Trust network access model for a hybrid-cloud scenario |
| SE03 | Lab: Design an IAM architecture for a fictional organisation; document privileged access controls |
| SE03 | Lab: Configure federated identity with SAML 2.0 or OIDC in a lab environment |
| SE04 | Lab: Design a SIEM deployment — define data sources, normalisation, correlation rules |
| SE04 | Lab: Build a SOAR playbook for a common incident type (e.g., phishing triage) |
| SE05 | Lab: Audit an Infrastructure-as-Code template (Terraform) against CIS benchmarks |
| SE05 | Lab: Integrate a SAST/DAST tool into a sample CI/CD pipeline |
| SE06 | Capstone: Design and document a secure architecture for a fictional Australian financial institution |

**Tools for this major (free or free-tier preferred):**
- Microsoft Threat Modelling Tool (free)
- draw.io / Excalidraw (architecture diagrams)
- Terraform (IaC — open-source)
- Checkov (IaC security scanning — open-source)
- Semgrep (SAST — free tier)
- n8n or Shuffle (open-source SOAR)
- OpenSSL, Keycloak (IAM / PKI)

---

## Australian Context

- [ ] **SE01** — ASD Essential Eight secure configuration requirements
- [ ] **SE02** — Australian Signals Directorate security architecture guidance; IRAP assessment framework
- [ ] **SE03** — APRA CPS 234 access control requirements; Privacy Act 1988 data handling in IAM design
- [ ] **SE05** — ASD Essential Eight application control, patching, and multi-factor authentication in DevSecOps
- [ ] **SE06** — Capstone should reference APRA CPS 234, ASD Essential Eight, and relevant Australian sector regulations

---

## Capstone Unit (SE06) Requirements

The capstone must produce a **secure architecture design document**:

- [ ] Fictional (or anonymised) Australian organisation with defined sector context
- [ ] Business requirements and security requirements documented
- [ ] Architecture diagrams produced (logical + physical + data flow)
- [ ] Threat model produced for the architecture
- [ ] Zero Trust principles applied and documented
- [ ] IAM architecture designed
- [ ] Relevant Australian regulatory requirements mapped (APRA, ASD, Privacy Act)
- [ ] Security control selection documented with rationale
- [ ] Risk register produced for residual risks
- [ ] Community practitioner review of the capstone
- [ ] Deliverable suitable for professional portfolio (reference `templates/student-portfolio/index.html`)

---

## Cross-Pathway Note

Security Engineering is the strategic major most dependent on operational knowledge. Units SE04 (Detection & Response Engineering) and SE05 (Cloud & DevSecOps) benefit strongly from:
- OC02 (Security Monitoring & SIEM)
- OC06 (Offensive Security Concepts)

Consider recommending these as electives for strategic students pursuing this major.

---

## Sign-off Requirements

Before any unit can be merged:

- [ ] Domain Expert with active security architecture or engineering experience named in metadata
- [ ] Practitioner Reviewer (different from Domain Expert) named in metadata
- [ ] SABSA references verified for accuracy
- [ ] Zero Trust architecture guidance verified against NIST SP 800-207 (2020)
- [ ] IaC lab configurations tested in the minimum hardware environment

See `templates/review-checklist.md` for the full pre-merge checklist.
