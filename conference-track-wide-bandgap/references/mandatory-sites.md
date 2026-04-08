# Mandatory Source Families

Check every source family in this list on every invocation, even if broad search results already look sufficient.

Primary role of this file:

- find newly surfaced conference families
- find new stable anchors that can be added back into `seed-conference-families.md`
- supplement the seed pool over time

Do not use this file as the main authority for whether a seed conference family should appear in the output.

This file is only for information sources and entry points.

Do not use this file to define which conferences belong in the long-term pool.
Conference families belong in `seed-conference-families.md`.

Use the following source tiers:

- `A-tier stable forced sources`: must review every run
- `B-tier discovery sources`: useful for supplement and expansion, but not required every run
- `C-tier excluded weak sources`: do not keep as long-term source-pool entries

Core maintenance rule:

- keep `A-tier` very small, stable, and repeatable
- use `A-tier` only for broad source families that can surface multiple conference families
- move single-conference official domains and deep links into `seed-conference-families.md`
- keep temporary registration links, questionnaires, and office-doc pages out of the long-term source pool
- use weak temporary pages only as one-off supporting evidence inside a specific run

## A-tier Stable Forced Sources

### Industry Media And Event Operators

- Source family: industry media and operator-style discovery domains
- Primary URLs:
  - https://www.fsemi.tech/cms/semiconductor.html
  - https://www.fsemi.tech/cms/xinwenkuaixun.html
  - https://www.hjssemi.com/ev/list
  - https://www.icsmart.cn/
- Usage:
  - use to find clues, invitation notices, or references to organizer pages
  - do not treat media coverage alone as the sole basis for important conference families
- Why included: useful for supplement and expansion

### Major Semiconductor Exhibition And Summit Domains

- Source family: large semiconductor exhibition and summit organizer domains
- Primary URLs:
  - https://www.semiconchina.org/
- Backup approach:
  - search current-edition forum pages, concurrent-event overview pages, summit sections, and exhibitor-news sections on the same domains
- Why forced: this domain can surface multiple domestic conference families,同期活动, and organizer-level updates

## B-tier Discovery Sources

## C-tier Excluded Weak Sources

Do not keep these as long-term source-pool entries.
They may appear as one-off evidence in a specific run, but they should not stay inside `mandatory-sites.md`.

- questionnaire pages such as `wjx.top`
- temporary office-doc pages such as `kdocs.cn`
- short-lived landing pages such as `s.31url.cn`
- event registration hosts such as `31113.scimeeting.cn`
- event registration hosts such as `chinanosz.7-event.cn`
- event registration hosts such as `casconf.cn`
- topic sites that mostly behave like carry pages or event-operation pages rather than reusable organizer sources
- temporary form hosts and poster-only links
- ad-hoc document links with no stable organizer domain behind them

Reason:

- low search value
- low durability
- weak structure
- poor repeatability across runs

## Maintenance Rules

- prefer stable organizer domains over single-page registration or agenda links
- prefer official association, organizer, exhibition, and society domains over article or landing-page URLs
- keep `A-tier` focused on a very small set of broad source families that can surface multiple conference families
- keep `B-tier` for discovery and supplement, not as the primary authority
- do not re-add questionnaire, office-doc, or short-link pages into `A-tier`
- do not promote a topic page into `A-tier` if it mostly behaves like a carrying page, registration page, or weak event landing page
- if a source repeatedly fails to produce reusable conference data, demote or remove it
- do not duplicate seed-specific deep links or single-conference official domains inside `mandatory-sites.md`; keep broader source-family entry points here and keep detailed page anchors in `seed-conference-families.md`
