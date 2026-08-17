# SynthOps Architecture

## Overview

SynthOps is an open-source synthetic operational data generation framework.

The project is designed to generate realistic, structured and fictional datasets for analytics engineering, business intelligence, AI prototyping and decision-intelligence use cases.

SynthOps is intentionally built as a modular system. The core generation logic is kept separate from domain-specific generation rules so that the project can start with Adult Social Care and later expand into other operational domains such as finance operations, construction operations, SaaS metrics and workforce analytics.

---

## Architectural Goals

The architecture is designed to support:

- maintainability
- modularity
- testability
- reproducibility
- responsible synthetic data generation
- domain extensibility
- analytics-ready output
- clear documentation
- future open-source contribution

SynthOps should be understandable enough for new contributors to explore, but structured enough to grow beyond a single script or tutorial project.

---

## High-Level Architecture

```text
SynthOps
├── Core Engine
│   ├── reusable ID generation
│   ├── reusable date utilities
│   ├── shared validation utilities
│   └── future export helpers
│
├── Domain Modules
│   ├── Adult Social Care
│   ├── Finance Operations planned
│   ├── Construction Operations planned
│   └── SaaS Metrics planned
│
├── Examples
│   └── runnable scripts showing how to generate sample datasets
│
├── Tests
│   └── automated checks for generator behaviour and data quality rules
│
└── Documentation
    └── project, architecture, domain and responsible-use guidance
```

---

## Repository Structure

```text
synthops/
├── data/
│   └── sample/
│       └── adult_social_care/
│
├── docs/
│   ├── domains/
│   ├── architecture.md
│   ├── ethical_use_and_limitations.md
│   ├── project_brief.md
│   └── roadmap.md
│
├── examples/
│   └── generate_adult_social_care_sample.py
│
├── notebooks/
│
├── src/
│   └── synthops/
│       ├── core/
│       │   ├── dates.py
│       │   └── ids.py
│       │
│       └── domains/
│           └── adult_social_care/
│               └── care_homes.py
│
├── tests/
│   ├── test_core_dates.py
│   ├── test_core_ids.py
│   ├── test_environment.py
│   └── test_adult_social_care_care_homes.py
│
├── README.md
├── ARCHITECTURE.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

---

## Core Engine

The `core` package contains logic that should be reusable across all domains.

Current core modules include:

| Module | Responsibility |
|---|---|
| `ids.py` | Generates readable synthetic IDs with configurable prefixes and widths |
| `dates.py` | Provides reusable date parsing, date range and random date utilities |

The core engine should remain domain-neutral.

For example, ID generation is not specific to adult social care. The same ID utility can support:

```text
HOME0001
HM001
RES00001
STAFF0001
CUS0001
INV000001
PRJ001
```

This prevents duplicated logic and keeps future domain modules consistent.

---

## Domain Modules

Domain modules contain industry-specific generation rules.

Each domain defines:

- entities and tables
- domain-specific assumptions
- relationships between entities
- realistic value ranges
- scenario controls
- data quality rules
- sample output

The first domain module is:

```text
adult_social_care
```

Future planned domains may include:

```text
finance_operations
construction_operations
saas_metrics
workforce_analytics
```

This structure allows SynthOps to grow without tightly coupling the entire project to adult social care.

---

## Adult Social Care Module

The Adult Social Care module is the first implemented domain.

It is designed to generate fictional but operationally plausible adult social care datasets.

Current implemented table:

```text
care_homes
```

Planned tables include:

```text
residents
resident_care_needs_history
staff
shifts
incidents
observations
handover_notes
```

The Adult Social Care module is intentionally treated as the first domain module, not as the whole product. This keeps SynthOps open to future domains while still allowing the first module to be realistic and useful.

---

## Current Data Generation Flow

The current generation flow is:

```text
User runs example script
        ↓
example script calls domain generator
        ↓
domain generator uses core utilities
        ↓
generator returns a pandas DataFrame
        ↓
example script writes sample CSV output
        ↓
tests verify expected behaviour and data quality rules
```

Current example:

```text
examples/generate_adult_social_care_sample.py
```

Current sample output:

```text
data/sample/adult_social_care/care_homes.csv
```

---

## Scenario-Driven Generation

SynthOps should not generate purely random data.

The project uses scenario-driven generation, where user-selected or generated scenario attributes influence downstream data.

In the Adult Social Care module, `care_home_type` and `turnover_profile` are early examples of scenario drivers.

For example:

- care home type influences occupancy behaviour
- turnover profile will influence resident lifecycle generation
- future resident care needs will influence incidents, observations and handover notes

This makes the generated data more realistic and more useful for analytics.

---

## Current Adult Social Care Scenario Drivers

The current `care_homes` generator supports:

| Scenario Driver | Purpose |
|---|---|
| `care_home_type` | Allows generation of Residential, Nursing, Dementia, Residential and Nursing, or Specialist Care homes |
| `turnover_profile` | Supports Stable, Moderate, High or Variable turnover assumptions |
| `id_prefix` | Allows users to customise generated ID prefixes |
| `id_width` | Allows users to customise generated ID length |
| `seed` | Supports reproducible generation |

These controls make SynthOps more useful for users generating data for a specific scenario, such as a single dementia care home or a mixed portfolio of care homes.

---

## Data Modelling Principles

SynthOps follows these modelling principles:

### 1. Separate stable entities from time-varying history

A resident record should not permanently store fields that change over time, such as falls risk or dependency level.

Instead:

- `residents` should store lifecycle information
- `resident_care_needs_history` should store changing care needs over time

This supports realistic longitudinal datasets.

### 2. Store base facts before derived fields

Raw generated data should store base facts where possible.

For example, the residents table should store:

```text
date_of_birth
admission_date
exit_date
```

Instead of storing only:

```text
current_age
age_band
length_of_stay
```

Those derived fields can be created later during transformation.

### 3. Preserve referential integrity

Child tables must link to valid parent records.

For example:

- every resident must belong to an existing care home
- every care-needs assessment must belong to an existing resident
- every incident must belong to a valid resident, care home and date

### 4. Use synthetic assumptions responsibly

SynthOps uses assumptions to create plausible variation.

These assumptions are not official statistics and should not be interpreted as real-world benchmarks.

---

## Testing Strategy

SynthOps uses `pytest` to test generator behaviour.

Current tests cover:

- environment setup
- core ID generation
- core date utilities
- care home generation
- custom ID formatting
- valid care home scenario controls
- invalid care home scenario controls
- occupancy bounds
- unique IDs
- unique care home names
- resident counts not exceeding bed capacity

The testing approach will expand as more domain tables are added.

Future tests should verify:

- referential integrity
- date validity
- lifecycle consistency
- realistic value ranges
- reproducible outputs when using seeds
- relationship rules between generated tables

---

## Extensibility Plan

SynthOps is designed so future domains can be added without rewriting the core engine.

A future domain should follow this pattern:

```text
src/synthops/domains/new_domain/
├── __init__.py
├── generator_module_1.py
├── generator_module_2.py
└── generate.py
```

Each new domain should include:

- source code
- tests
- documentation
- sample output
- example script
- clearly documented assumptions

This keeps each domain self-contained while still sharing the same SynthOps core utilities.

---

## Current Limitations

SynthOps is currently in early development.

Current limitations include:

- only the Adult Social Care domain has started implementation
- only the `care_homes` table is implemented
- no command-line interface yet
- no Streamlit or web interface yet
- no automated CI/CD workflow yet
- no release version has been published yet
- generated assumptions are synthetic and not sector benchmarks

These limitations are expected at this stage and are tracked through the project roadmap.

---

## Future Architecture Direction

Planned architecture improvements include:

- central configuration objects
- domain-level generation orchestration
- CSV and Parquet export options
- validation utilities for generated datasets
- command-line interface
- GitHub Actions for automated tests
- documentation site using GitHub Pages or MkDocs
- contribution workflow for external users
- versioned releases

---

## Summary

SynthOps is designed as a modular synthetic data generation framework, not a single-purpose script.

The architecture separates reusable core utilities from domain-specific generation logic, allowing Adult Social Care to act as the first domain module while preserving a path toward finance, construction, SaaS and other operational domains.

This structure supports the long-term goal of building a professional, maintainable and useful open-source analytics project.