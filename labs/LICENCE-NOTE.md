# Licensing of the lab directory

The repository as a whole is **CC BY 4.0**, which is right for curriculum prose
and wrong for executable code — CC licences are not designed for software and
carry no patent or warranty terms.

So this directory is dual-licensed by content type:

| Path | Licence | Why |
|---|---|---|
| `generator/`, `harness/`, `docker/`, `splunk-apps/` | **MIT** | Executable code. MIT lets other educators reuse the generator in unrelated courses without attribution friction. |
| `guides/`, `docs/`, this file, `README.md` | **CC BY 4.0** | Prose, consistent with the rest of the repository. |
| `data/` | Not licensed — not committed | Generated output, reproducible from a seed. |

**Not legal advice.** This split is the maintainers' reading of common practice
for mixed content/code educational repositories. A delivery partner intending to
redistribute should have it reviewed. Recorded as an open item in
[`docs/TODO.md`](../docs/TODO.md).

## Third-party

The lab pulls the official `splunk/splunk` container image. Splunk is a
trademark of its owner; this project is not affiliated with or endorsed by
Splunk. Use of the image is governed by Splunk's own licence, accepted
explicitly in the compose files. No Splunk code, courseware or test content is
redistributed here.
