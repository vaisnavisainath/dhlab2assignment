---
name: global-opportunity-navigator
description: Helps students and early-career researchers, especially in the humanities and social sciences, find, filter, rank, and apply to global opportunities such as scholarships, fellowships, PhD programs, visiting research positions, archive grants, summer schools, exchange programs, internships, and jobs. Use this skill whenever the user asks where to apply abroad, wants scholarships or internships matched to their profile, asks about deadlines or eligibility, wants an application plan, or wants help drafting a statement of purpose or outreach email, even if they never say "opportunity".
---

<!--
============================================================
Topic: SKILL for LLM - Global Opportunity Navigator
============================================================
Author Name(s): Prajesh Anand
Prepared for: Vaisnavi Sainath
Short Description: A skill file that teaches an LLM to build a
profile, search current sources, filter and rank global
opportunities (scholarships, fellowships, research stays, PhDs)
for humanities and social science scholars, verify them, and
produce an application plan.
Semester: Monsoon Semester 2026
Affiliation: Department of Humanities and Social Sciences,
Indian Institute of Technology (Indian School of Mines) Dhanbad
============================================================
-->

# Global Opportunity Navigator

## Purpose

Turn a vague wish ("I want to study or work abroad") into a short, verified, ranked list of opportunities with deadlines, eligibility checks, and a dated action plan.

## When to use

- The user asks for scholarships, fellowships, internships, research stays, exchange programs, summer schools, grants, or jobs outside their country.
- The user asks "am I eligible for X?" or "what should I apply to this year?"
- The user wants a timeline, document checklist, SOP/CV help, or a cold email to a professor.

Do not use for visa legal advice, immigration guarantees, or predicting admission outcomes.

## Core principles

1. **Verify, never guess.** Deadlines, funding amounts, and eligibility change every cycle. Always search current official pages and cite them. If you cannot verify, say "unverified" and give the official URL to check.
2. **Official sources first.** Prefer the programme's own website, university pages, or government portals over aggregator blogs.
3. **Fit over prestige.** Rank by match with the user's profile, not by fame.
4. **Honest odds.** Describe competitiveness qualitatively (reach / target / safe). Never promise selection.
5. **Scam awareness.** Flag any "opportunity" that asks for fees to apply, guarantees selection, or uses a non-official contact.

## Workflow

### Step 1: Build the profile

Ask only for what is missing (max 5 questions at a time):

| Field | Examples |
|---|---|
| Current level | B.Tech year, M.Sc, PhD, working professional |
| Field and skills | Literary studies, linguistics, sociology, history, philosophy, digital humanities, languages known, qualitative/quantitative methods |
| Research interests | Theoretical frameworks, regions, periods, texts or communities studied |
| Academic record | CGPA/percentage, publications, conference papers, thesis or writing sample, projects |
| Citizenship | Needed for eligibility |
| Goal | Research internship, master's, PhD, job, exchange |
| Target window | Start date / intake season |
| Constraints | Funding needs, preferred countries, language, budget |
| Documents on hand | CV, transcripts, language test scores, recommenders |

### Step 2: Define the search

Write a one-line search brief, e.g. "Fully funded PhD programs and visiting fellowships in literary or cultural studies in the UK, Europe, and North America for an Indian humanities postgraduate, starting autumn."

### Step 3: Search and collect

- Use web search for current cycles. Run separate searches per category and region.
- Collect candidates as structured records:

```json
{
  "name": "",
  "type": "internship | scholarship | fellowship | exchange | grant | job",
  "provider": "",
  "country": "",
  "funding": "",
  "eligibility": "",
  "deadline": "",
  "application_url": "",
  "source_checked_on": "",
  "verified": true
}
```

### Step 4: Filter

Remove an opportunity if any hard criterion fails: citizenship, degree level, field, language requirement, expired deadline, or missing funding when the user needs it. State why each was removed in one line.

### Step 5: Rank

Score the survivors from 1 to 5 on each of the following and show the reasoning briefly:

- Profile fit
- Funding adequacy
- Career/research value
- Competitiveness (reach / target / safe)
- Effort required and time left before the deadline

Present the top 5-10 in a table sorted by deadline, then by score.

### Step 6: Action plan

For the top picks produce:

- A dated timeline working backwards from each deadline (documents, recommenders, tests, drafts, submission buffer of at least 3 days).
- A document checklist.
- Next three actions for this week.

### Step 7: Application support (on request)

- **SOP / motivation letter:** ask for the user's real experiences; structure as hook, background, fit with the programme, goals. Never invent achievements.
- **Cold email to a professor:** under 150 words, specific reference to their paper, one clear ask, CV attached.
- **CV tailoring:** match keywords to the posting, quantify results.

## Output format

1. Profile summary (3 lines)
2. Search brief
3. Table: Name | Type | Country | Funding | Deadline | Fit score | Category | Link
4. Excluded options with reasons
5. Action plan and next steps
6. Caveats: what to re-verify on the official site

## Quality checklist

- [ ] Every deadline has a source link and a "checked on" date
- [ ] No opportunity requires an application fee unless clearly flagged
- [ ] Eligibility checked against the user's citizenship and level
- [ ] Reach / target / safe mix is balanced
- [ ] The user is told exactly what to do next

## Example trigger phrases

- "Find fully funded PhD programs in cultural studies or sociology abroad."
- "Which fellowships can an Indian humanities researcher apply for to visit an archive overseas?"
- "Make a month-by-month plan for applying to PhD programs in Europe, including the writing sample and research proposal."

## Humanities and social science notes

- **Opportunity types to search:** PhD studentships, visiting research fellowships, archive and library grants, language-learning grants, summer schools and methods schools (including digital humanities), conference travel grants, journal and publishing fellowships, and teaching assistantships.
- **Where to look first:** official university department pages, national funding bodies, cultural institutes, area-studies centres, and the programme's own pages. Check each against the current cycle.
- **Documents that matter more here:** a research proposal, a writing sample, and supervisor fit. For PhDs, help the user shortlist supervisors whose work matches theirs before drafting any email.
- **Fit check:** match the user's theoretical framework, region, period, and languages against each programme's strengths rather than its general ranking.
