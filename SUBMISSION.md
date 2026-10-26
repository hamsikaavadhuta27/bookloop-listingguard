# Competition Submission: BookLoop ListingGuard

**Event:** Build for AI Agents: LLM SkillHub Student Challenge 2026  
**Track:** Education & Student Utilities / Task-Oriented Agent Skills  
**Skill Name:** `bookloop-listingguard`  
**Author:** BookLoop Developer Team  
**Status:** Ready for final review and submission

---

## 1. Executive Summary

### Problem Statement

University and engineering students often have surplus textbooks after completing semesters. Selling directly to other students can make books more affordable for buyers and give sellers greater flexibility. However, listings may be incomplete, omit edition details, hide defects, or contain contradictory information. Buyers then need to ask repeated questions and may purchase editions that do not match their course requirements. Guessing authors, publication years, or ISBNs can also reduce trust.

### Target Audience

1. **University and college student sellers:** Students who want to create accurate textbook listings quickly.
2. **Student buyers:** Students looking for affordable textbooks with clear edition information and honest condition disclosures.
3. **Campus exchange communities:** Student unions, campus book-exchange platforms such as BookLoop, and student developer communities.

### How BookLoop ListingGuard Solves the Problem

BookLoop ListingGuard is a reusable AI-agent skill that helps compatible AI coding assistants and CLI agents audit and prepare second-hand textbook listings. It follows a structured workflow organized into seven stages (Stages A–G), covering these core capabilities:

1. **Factual Extraction:** Organizes provided information into 13 standardized listing fields.
2. **Prioritized Follow-ups:** Groups missing information into concise questions without unnecessarily repeating supplied facts.
3. **Anti-Hallucination Guardrails:** Prohibits inventing authors, editions, ISBNs, publishers, or syllabus matches.
4. **Contradiction Detection:** Flags conflicting details, such as mismatched course information or claims of pristine condition alongside reported markings.
5. **Standardized Drafting:** Produces a structured 13-field listing with a defined status, such as `Needs more information`, `Draft ready for seller review`, or `Ready to publish, subject to the platform's requirements`.
6. **Marketplace Safety:** Avoids unsupported price guarantees and encourages seller-confirmed public campus exchange locations.
7. **Uncertainty Handling and Review:** Keeps unverified information clearly labeled and requires seller review before a listing is treated as ready for publication.

### Improvements After Testing

Eight individual test scenarios were used to evaluate incomplete listings, unknown editions, contradictory information, complete listings, defect disclosure, unsupported price guarantees, academic relevance, and requests to fabricate book details. The skill was refined to handle unknown information more explicitly and to distinguish reported facts from unverified details.

---

## 2. Key Architectural Features

- **Progressive Questioning:** Groups missing information into concise follow-up questions.
- **13-Field Listing Schema:** Standardizes listing information for easier review and reuse.
- **Contradiction Detection:** Flags discrepancies in book details and physical condition.
- **Privacy and Safety Guidance:** Avoids including private phone numbers, banking details, and residential addresses in public listings.
- **Uncertainty Labels:** Marks missing or unverified information instead of presenting guesses as facts.

---

## 3. Scope, Boundaries, and Limitations

1. **No automatic database verification:** The skill works from the information available in the agent's context. Live ISBN, bookstore, or syllabus verification requires appropriate external tools and reliable sources.
2. **No guaranteed sale prices:** It does not guarantee a market price or a sale within a specific time. Price guidance should be treated as advisory.
3. **No autonomous publishing:** Listing drafts require seller review. The skill does not claim a listing is live without a connected, authorized publishing mechanism and confirmation.
4. **No syllabus certification:** It does not certify that a book matches a course syllabus without a reliable curriculum reference.
5. **Seller confirmation matters:** Physical condition, defects, edition details, and exchange arrangements should not be treated as verified unless supported by the seller's information.

---

## 4. Evaluation and Testing Evidence

The skill was evaluated using eight manually executed test scenarios covering incomplete listings, unknown editions, contradictory information, complete listings, defect disclosure, unsupported price guarantees, academic relevance verification, and requests to fabricate book details.

The observed results and minor issues are documented in `EVALUATION.md`. These tests informed improvements to uncertainty handling, defect disclosure, exchange-location details, condition grading, and inferred academic information.

The tests represent individual scenario-based evaluations. No formal user study or student-participant testing is claimed.

A separate Python validation script checks the skill's structure and simulates benchmark outcomes. Its simulated score is not presented as independent proof that every live AI response passes every scenario.

---

## 5. Submission Checklist and Next Actions

### Verify the project files

- `SKILL.md` — Main skill specification with YAML frontmatter.
- `EVALUATION.md` — Test scenarios, scoring rubric, and observed results.
- `SUBMISSION.md` — Project summary and submission documentation.
- `scripts/validate_skill.py` — Structural validator and simulated benchmark runner.
- `.agents/skills/bookloop-listingguard/SKILL.md` — Workspace copy of the skill, checked against the main file.

### Publish to a Git repository

After confirming the correct repository URL and reviewing the files, initialize Git if needed:

```bash
git init
git add SKILL.md EVALUATION.md SUBMISSION.md scripts/ .agents/
git commit -m "feat: complete BookLoop ListingGuard skill"
```

Create a GitHub repository, then connect it using your actual repository URL:

```bash
git remote add origin https://github.com/YOUR-USERNAME/bookloop-listingguard.git
git branch -M main
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If the remote already exists, check it before adding another.

### SkillHub publication

Check the competition's official instructions for the supported publication method and CLI requirements before running:

```bash
llmsh publish . --name bookloop-listingguard
```

Run this command only if the required CLI is installed and the competition instructions confirm this is the correct command.

### Competition portal submission

On the competition portal:

- **Skill Name:** BookLoop ListingGuard
- **Public Skill Link:** Add the actual public GitHub or SkillHub link after publication.
- **Written Summary:** Use the executive summary above, checking the portal's word limit.
- **Evidence and Evaluation:** Attach or link `EVALUATION.md` and any actual test logs requested by the organizers.

Do not submit placeholder URLs or claim publication until it has been completed and verified.
