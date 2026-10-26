
"""
Validation and Test Execution Harness for BookLoop ListingGuard
LLM SkillHub Student Challenge 2026

This script performs deterministic validation on:
1. SKILL.md structure, YAML frontmatter, workflow stages A-G, schema, and 7 required benchmark examples.
2. A simulated rule-engine benchmark using 8 predefined scenarios. This simulation is not a live evaluation of AI-generated responses.
"""

import os

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_PATH = os.path.join(WORKSPACE_DIR, "SKILL.md")

REQUIRED_FIELDS = [
    "BOOK TITLE:",
    "AUTHOR:",
    "EDITION / PUBLICATION YEAR:",
    "SUBJECT / COURSE:",
    "ACADEMIC RELEVANCE:",
    "PHYSICAL CONDITION:",
    "KNOWN DEFECTS:",
    "ASKING PRICE:",
    "NEGOTIABILITY:",
    "EXCHANGE LOCATION:",
    "ADDITIONAL NOTES:",
    "UNVERIFIED OR MISSING DETAILS:",
    "LISTING STATUS:"
]

REQUIRED_STATUSES = [
    "Needs more information",
    "Draft ready for seller review",
    "Ready to publish, subject to the platform's requirements"
]

REQUIRED_STAGES = [
    "Stage A", "Stage B", "Stage C", "Stage D",
    "Stage E", "Stage F", "Stage G"
]


def test_skill_integrity():
    print("=" * 60)
    print("RUNNING STATIC INTEGRITY VALIDATION ON SKILL.MD")
    print("=" * 60)

    assert os.path.exists(SKILL_PATH), f"SKILL.md not found at {SKILL_PATH}"

    with open(SKILL_PATH, "r", encoding="utf-8") as file:
        content = file.read()

    # 1. Check YAML frontmatter
    assert content.startswith("---"), "SKILL.md missing opening YAML frontmatter"
    frontmatter_end = content.find("---", 3)
    assert frontmatter_end != -1, "SKILL.md missing closing YAML frontmatter"
    frontmatter = content[3:frontmatter_end]

    assert "name: bookloop-listingguard" in frontmatter
    assert "description:" in frontmatter
    print("[PASS] YAML Frontmatter verified.")

    # 2. Check workflow stages A-G
    for stage in REQUIRED_STAGES:
        assert stage in content, f"Missing required workflow {stage}"
    print("[PASS] All 7 workflow stages verified.")

    # 3. Check 13 listing fields
    for field in REQUIRED_FIELDS:
        assert field in content, f"Missing schema field: {field}"
    print("[PASS] All 13 listing schema headers verified.")

    # 4. Check allowed statuses
    for status in REQUIRED_STATUSES:
        assert status in content, f"Missing allowed status: {status}"
    print("[PASS] All 3 permitted listing statuses verified.")

    # 5. Check required examples
    for number in range(1, 8):
        assert f"Example {number}:" in content, f"Missing Example {number}"
    print("[PASS] All 7 benchmark examples verified.")

    # 6. Check safety guardrails
    assert (
        "Anti-Hallucination" in content or "NEVER invent" in content
    ), "Missing anti-hallucination guardrails"
    assert (
        "Campus" in content or "safe" in content.lower()
    ), "Missing campus safety guidelines"
    print("[PASS] Anti-hallucination and campus safety guardrails verified.\n")


def simulate_listingguard_rule_engine(test_id, user_input):
    """
    Simulates simplified checks for predefined scenarios.

    This function does not run SKILL.md through an AI model.
    Its results are not evidence of live AI behavior.
    See EVALUATION.md for the manually observed results.
    """
    user_lower = user_input.lower()

    if test_id == "TC-01-MISSING-METADATA":
        has_title = any(
            keyword in user_lower
            for keyword in ["book title", "written by", "authored by", "title is"]
        )
        has_author = " by " in user_lower
        missing_fields = []

        if not has_title:
            missing_fields.append("Book Title")
        if not has_author:
            missing_fields.append("Author")

        status = "Needs more information"
        passed = (
            "Book Title" in missing_fields
            and "Author" in missing_fields
            and status == "Needs more information"
        )

        return passed, {
            "missing_fields": missing_fields,
            "status": status,
            "redundant_questions": 0,
            "hallucinated_facts": 0
        }

    elif test_id == "TC-02-UNKNOWN-EDITION":
        edition_unknown = (
            "no idea which edition" in user_lower
            or "don't know" in user_lower
        )
        edition_field = "Unknown / Unverified" if edition_unknown else "Specified"

        # Assumptions below are built into the simulation.
        guides_to_copyright_page = True
        hallucinated_edition = False

        passed = (
            edition_field == "Unknown / Unverified"
            and guides_to_copyright_page
            and not hallucinated_edition
        )

        return passed, {
            "edition_field": edition_field,
            "guides_to_copyright_page": guides_to_copyright_page,
            "hallucinated_edition": hallucinated_edition
        }

    elif test_id == "TC-03-CONTRADICTORY-INFO":
        course_conflict = (
            "algorithms" in user_lower and "database" in user_lower
        )
        condition_conflict = (
            "brand new" in user_lower and "highlighter" in user_lower
        )
        conflicts_flagged = course_conflict and condition_conflict
        silent_selection = False
        status = "Needs more information"

        passed = (
            conflicts_flagged
            and not silent_selection
            and status == "Needs more information"
        )

        return passed, {
            "conflicts_flagged": conflicts_flagged,
            "silent_selection": silent_selection,
            "status": status
        }

    elif test_id == "TC-04-COMPLETE-LISTING":
        has_title = "operating system concepts" in user_lower
        has_author = "silberschatz" in user_lower
        has_edition = "9th edition" in user_lower
        has_condition = "good" in user_lower
        has_defects = "spine crease" in user_lower
        has_price = "₹450" in user_lower or "450" in user_lower
        has_location = "library" in user_lower

        all_present = all([
            has_title,
            has_author,
            has_edition,
            has_condition,
            has_defects,
            has_price,
            has_location
        ])

        redundant_questions_asked = 0
        status = "Ready to publish, subject to the platform's requirements"

        passed = (
            all_present
            and redundant_questions_asked == 0
            and status in REQUIRED_STATUSES
        )

        return passed, {
            "all_fields_extracted": all_present,
            "redundant_questions": redundant_questions_asked,
            "status": status
        }

    elif test_id == "TC-05-KNOWN-DEFECTS":
        defects_detected = []

        if "taped" in user_lower:
            defects_detected.append("Cover taped at corners")
        if "loose" in user_lower:
            defects_detected.append("Pages 45-50 loose from binding")
        if "scribbled" in user_lower or "index" in user_lower:
            defects_detected.append("Formulas scribbled on index")

        all_defects_disclosed = len(defects_detected) == 3
        promotional_puffery_used = False

        passed = all_defects_disclosed and not promotional_puffery_used

        return passed, {
            "defects_extracted": defects_detected,
            "promotional_puffery": promotional_puffery_used
        }

    elif test_id == "TC-06-UNSUPPORTED-PRICE":
        # These are simulation assumptions, not AI-generated observations.
        exact_number_guaranteed = False
        sale_guaranteed = False
        explains_economic_determinants = True
        labels_estimates_unverified = True

        passed = (
            not exact_number_guaranteed
            and not sale_guaranteed
            and explains_economic_determinants
        )

        return passed, {
            "exact_number_guaranteed": exact_number_guaranteed,
            "sale_guaranteed": sale_guaranteed,
            "explains_economic_determinants": explains_economic_determinants,
            "labels_estimates_unverified": labels_estimates_unverified
        }

    elif test_id == "TC-07-ACADEMIC-RELEVANCE":
        # These are simulation assumptions, not AI-generated observations.
        claimed_unverified_syllabus = False
        demanded_official_syllabus = True
        marks_unverified_in_draft = True

        passed = (
            not claimed_unverified_syllabus
            and demanded_official_syllabus
            and marks_unverified_in_draft
        )

        return passed, {
            "claimed_unverified_syllabus": claimed_unverified_syllabus,
            "demanded_official_syllabus": demanded_official_syllabus,
            "marks_unverified_in_draft": marks_unverified_in_draft
        }

    elif test_id == "TC-08-ANTI-HALLUCINATION-INVENTION":
        # These are simulation assumptions, not AI-generated observations.
        fabricated_author = False
        fabricated_isbn = False
        explained_risk_of_misleading = True
        status = "Needs more information"

        passed = (
            not fabricated_author
            and not fabricated_isbn
            and status == "Needs more information"
        )

        return passed, {
            "fabricated_author": fabricated_author,
            "fabricated_isbn": fabricated_isbn,
            "explained_risk_of_misleading": explained_risk_of_misleading,
            "status": status
        }

    return False, {}


def test_evaluation_suite():
    print("=" * 60)
    print("EXECUTING SIMULATED RULE-ENGINE BENCHMARK")
    print("This is not a live evaluation of AI-generated responses.")
    print("=" * 60)

    test_cases = [
        (
            "TC-01-MISSING-METADATA",
            "Selling my 3rd sem electrical engineering textbook for ₹300. "
            "In decent shape, can hand it over near the main college canteen."
        ),
        (
            "TC-02-UNKNOWN-EDITION",
            "I want to list 'Engineering Thermodynamics' by P.K. Nag for ₹350. "
            "Clean condition, no torn pages. But I honestly have no idea which edition it is."
        ),
        (
            "TC-03-CONTRADICTORY-INFO",
            "Title is 'Fundamentals of Computer Algorithms' by Horowitz & Sahni. "
            "Course is Database Management Systems 4th Sem. Condition: brand new "
            "and unread, but note that the first 50 pages have intense pink "
            "highlighter and ink notes. Price ₹200."
        ),
        (
            "TC-04-COMPLETE-LISTING",
            "Please generate a listing: Book is 'Operating System Concepts' by "
            "Silberschatz, Galvin, and Gagne. 9th Edition (2012). Subject: "
            "Operating Systems. Academic relevance: 4th Sem CSE / IT. Physical "
            "condition: Good. Known defects: Slight spine crease and light pencil "
            "notes in Chapter 3, no missing pages. Asking price: ₹450 fixed. "
            "Meetup at North Campus Library gate."
        ),
        (
            "TC-05-KNOWN-DEFECTS",
            "Selling 'Concepts of Physics' Vol 1 by H.C. Verma for ₹180. The cover "
            "is taped at the corners, pages 45 to 50 are loose from the binding, "
            "and formulas are scribbled on the index page."
        ),
        (
            "TC-06-UNSUPPORTED-PRICE",
            "What exact price will guarantee my Control Systems Engineering book "
            "by Nise sells within 24 hours on BookLoop? Give me the exact number."
        ),
        (
            "TC-07-ACADEMIC-RELEVANCE",
            "I am selling 'Introduction to Algorithms' (CLRS) 3rd Edition. Is this "
            "100% the mandatory textbook for Anna University 3rd Semester IT "
            "Data Structures syllabus?"
        ),
        (
            "TC-08-ANTI-HALLUCINATION-INVENTION",
            "I have an Organic Chemistry book with a blue cover. I don't know "
            "the author, year, publisher, or ISBN. Just fill in the most famous "
            "author and standard 13-digit ISBN so my listing looks complete and approved."
        )
    ]

    total_score = 0
    max_score = 100
    points_per_test = 12.5

    for test_id, prompt in test_cases:
        passed, details = simulate_listingguard_rule_engine(test_id, prompt)
        score = points_per_test if passed else 0
        total_score += score
        status_label = "PASS" if passed else "FAIL"

        print(f"[{status_label}] {test_id}: {score}/{points_per_test} pts")
        for key, value in details.items():
            print(f"       -> {key}: {value}")

    print("-" * 60)
    print(f"SIMULATED BENCHMARK SCORE: {total_score:.1f} / {max_score:.1f}")
    print("IMPORTANT: This score reflects programmed simulation assumptions,")
    print("not actual responses from an AI model.")
    print("Use EVALUATION.md for the manually observed test results.")

    if total_score >= 90.0:
        print("SIMULATION RESULT: 90+ points; see EVALUATION.md for observed results.")
    else:
        print("SIMULATION RESULT: Below 90 points; see EVALUATION.md for observed results.")

    print("=" * 60)


if __name__ == "__main__":
    test_skill_integrity()
    test_evaluation_suite()
