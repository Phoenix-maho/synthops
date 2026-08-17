# SynthOps Roadmap

## Overview

SynthOps is being developed as a professional open-source synthetic operational data generation framework.

The project is designed to support analytics engineering, business intelligence, AI prototyping and decision-intelligence use cases by generating realistic, structured and fictional operational datasets across multiple domains.

The roadmap is organised into phases so the project can mature from a focused early prototype into a maintainable open-source product.

---

## Roadmap Principles

SynthOps development is guided by the following principles:

- build a useful product, not just a portfolio project
- prioritise maintainability and clarity
- keep the core engine domain-neutral
- keep domain-specific logic modular
- document assumptions transparently
- avoid using real personal or confidential data
- support realistic operational relationships
- create analytics-ready outputs
- use tests to protect data quality rules
- make the project understandable for future contributors

---

## Phase 1: Repository Foundation

**Goal:** Make the repository clear, credible and understandable before expanding the generator.

### Planned work

- [x] Create initial repository structure
- [x] Add Python package layout
- [x] Add initial README
- [x] Add architecture documentation
- [ ] Add roadmap documentation
- [ ] Add contributing guidelines
- [ ] Add changelog
- [ ] Add security policy
- [ ] Add code of conduct
- [ ] Add adult social care domain documentation
- [ ] Add architecture diagrams
- [ ] Add data flow diagrams

### Outcome

By the end of Phase 1, a visitor should understand:

- what SynthOps is
- why it exists
- how the repository is organised
- how the architecture supports multiple domains
- what has been built so far
- what is planned next
- how the project handles responsible synthetic data use

---

## Phase 2: Generator Implementation

**Goal:** Build tested, documented and reusable generator capabilities.

### Completed

- [x] Core ID generation utilities
- [x] Core date utilities
- [x] Scenario-driven adult social care home generator
- [x] Sample `care_homes.csv` output
- [x] Tests for current generator behaviour

### Planned Adult Social Care tables

- [ ] `residents`
- [ ] `resident_care_needs_history`
- [ ] `staff`
- [ ] `shifts`
- [ ] `incidents`
- [ ] `observations`
- [ ] `handover_notes`

### Planned technical improvements

- [ ] Domain-level generation orchestration
- [ ] Configurable dataset periods
- [ ] CSV export helpers
- [ ] Parquet export support
- [ ] Dataset validation utilities
- [ ] Data dictionary documentation
- [ ] Sample Power BI dataset
- [ ] Example notebooks

### Outcome

By the end of Phase 2, SynthOps should generate a coherent Adult Social Care dataset with realistic relationships between homes, residents, care needs, staff, shifts, incidents and observations.

---

## Phase 3: Open-Source Product Management

**Goal:** Make SynthOps look and operate like an actively maintained open-source product.

### Planned work

- [ ] Create GitHub Project board
- [ ] Create GitHub milestones
- [ ] Create labelled GitHub issues
- [ ] Add issue templates
- [ ] Add pull request template
- [ ] Enable GitHub Discussions
- [ ] Publish first pre-release
- [ ] Write release notes
- [ ] Maintain changelog entries
- [ ] Add contributor guidance for new domain modules

### Proposed milestones

| Milestone | Focus |
|---|---|
| `v0.1.0` | Repository foundation and care homes generator |
| `v0.2.0` | Resident lifecycle and care needs history |
| `v0.3.0` | Staff, shifts and incidents |
| `v0.4.0` | Observations, handovers and sample dashboard dataset |
| `v1.0.0` | Stable Adult Social Care module |

### Outcome

By the end of Phase 3, SynthOps should have visible project management, clear contribution pathways and an early release history.

---

## Phase 4: Engineering Maturity

**Goal:** Improve reliability, automation and maintainability.

### Planned work

- [ ] Add GitHub Actions test workflow
- [ ] Run tests automatically on pull requests
- [ ] Add linting
- [ ] Add formatting
- [ ] Add type checking
- [ ] Add package versioning strategy
- [ ] Add release workflow
- [ ] Add documentation site
- [ ] Add dependency/security checks
- [ ] Add contribution review process

### Possible tools

- `pytest`
- `ruff`
- `mypy`
- `GitHub Actions`
- `MkDocs`
- `pre-commit`

### Outcome

By the end of Phase 4, SynthOps should have the quality gates expected of a serious open-source Python project.

---

## Future Domain Modules

SynthOps is designed to support multiple operational domains.

Possible future modules include:

### Finance Operations

Potential tables:

- customers
- products
- invoices
- payments
- revenue events
- cost centres
- forecasts
- targets

### Construction Operations

Potential tables:

- projects
- sites
- contractors
- assets
- inspections
- defects
- work packages
- progress updates

### SaaS Metrics

Potential tables:

- accounts
- users
- subscriptions
- usage events
- support tickets
- renewals
- churn events

### Workforce Analytics

Potential tables:

- employees
- roles
- departments
- shifts
- absence records
- performance events
- training records

---

## Current Priority

The current priority is to complete the Phase 1 repository foundation, then continue the Adult Social Care module with resident lifecycle generation.

Next planned development tasks:

1. Complete repository documentation foundation.
2. Create GitHub milestones and issues.
3. Design and implement `residents`.
4. Design and implement `resident_care_needs_history`.
5. Add data dictionary for Adult Social Care.
6. Add initial diagrams.
7. Prepare first pre-release.

---

## Responsible Development Note

SynthOps uses fictional synthetic data and synthetic modelling assumptions.

The project does not use real resident, patient, staff, provider, financial or organisational records.

Generated data should be used for learning, analytics development, dashboarding, testing and prototyping only. It should not be used for real-world decision-making about individuals, organisations, care quality, safeguarding, employment, finance or regulation.