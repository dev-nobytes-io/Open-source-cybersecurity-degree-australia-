# TODO — templates/student-portfolio/

This directory contains the student portfolio template — an HTML page that learners use to present their completed degree work to employers and the community.

**Files in this directory:**
- `index.html` — The portfolio HTML template

---

## Current State of index.html

The portfolio template exists as an HTML file. The following improvements should be made:

---

## Content Improvements

- [ ] **Add a section for every major** — the current template should have placeholder sections for all 8 majors so learners know exactly what to fill in regardless of which major they chose
- [ ] **Add a framework competency table** — a structured table showing:
  - DCWF T-codes demonstrated
  - SFIA skills at which level
  - ASD CSF domains covered
  This table is the employer-facing version of `templates/competency-profile-template.md`
- [ ] **Add a capstone project showcase section** — dedicated space for the capstone deliverable with:
  - Project summary
  - Link to the artefact (GitHub, PDF, etc.)
  - Practitioner review statement (confirming community review occurred)
- [ ] **Add a "degree pathway" visualisation** — a simple diagram showing which units were completed (Operational vs. Strategic, which major)
- [ ] **Add a certification bridge section** — where learners can list any industry certifications they hold that complement the degree
- [ ] **Add a "how I learned it" section per unit** — brief reflection on key skills developed per unit

---

## Technical Improvements

- [ ] **Ensure the HTML is valid and passes W3C validation**
- [ ] **Ensure WCAG 2.1 AA accessibility compliance:**
  - All images have alt text
  - Colour contrast meets minimum ratios
  - Keyboard navigation works throughout
  - Screen reader compatible headings and landmarks
- [ ] **Make the portfolio mobile-responsive** — learners may share this link from a phone; it must render correctly on all screen sizes
- [ ] **Remove any external CDN dependencies** — the portfolio should work without internet access (for learners who want a local/offline version)
- [ ] **Add a print stylesheet** — so the portfolio prints cleanly as a PDF for learners who want a paper version
- [ ] **Add a dark mode option** — simple `prefers-color-scheme` CSS

---

## Customisation Guidance

- [ ] **Add inline HTML comments** explaining what each section is for and how to customise it
- [ ] **Add a `README.md` in this directory** explaining:
  - How to deploy the portfolio (GitHub Pages, Netlify, or local file)
  - How to customise the CSS
  - How to add/remove sections
  - Licensing: the template is CC BY 4.0; learners own their own portfolio content
- [ ] **Add a `style.css` file** (separate from the HTML) so learners can customise styling without touching the HTML structure

---

## Future Additions

- [ ] **Consider a JSON/structured data version** — a `portfolio.json` file that learners fill in, with the HTML rendering it dynamically. This would allow automated processing of competency data.
- [ ] **GitHub Pages deployment instructions** — add a simple guide so learners can host their portfolio for free on GitHub Pages
- [ ] **Add employer instructions** — a brief note at the top of the portfolio (visually styled differently) explaining to employers what the degree is, how community review works, and how to verify a learner's framework competencies
