# Contributing to SynthOps

Thank you for your interest in contributing to SynthOps.

SynthOps is an open-source synthetic operational data generation framework designed to create realistic, structured and fictional datasets for analytics engineering, business intelligence, AI prototyping and decision-intelligence use cases.

The project is currently in early development. Contributions are welcome, especially around documentation, testing, domain modelling, data quality rules, examples and new synthetic data generation modules.

---

## Project Goals

SynthOps aims to:

- generate safe fictional datasets for analytics and prototyping
- support multiple operational domains through modular design
- keep the core engine domain-neutral
- keep domain-specific logic modular
- document synthetic assumptions clearly
- maintain realistic relationships between generated tables
- support reproducible data generation
- provide examples useful to analysts, analytics engineers, BI developers and data scientists

---

## Current Project Status

SynthOps is in early development.

The first domain module is:

```text
adult_social_care
```

Currently implemented tables:

```text
care_homes
residents
```

Planned Adult Social Care tables include:

```text
resident_care_needs_history
staff
shifts
incidents
observations
handover_notes
```

Future planned domains may include:

```text
finance_operations
construction_operations
saas_metrics
workforce_analytics
```

---

## Ways to Contribute

You can contribute by helping with:

- improving documentation
- adding tests
- reviewing data generation assumptions
- improving sample outputs
- suggesting realistic operational scenarios
- fixing bugs
- improving developer experience
- adding new domain modules
- adding example notebooks or dashboards
- improving validation rules
- improving diagrams and data dictionaries

---

## Responsible Synthetic Data Principles

SynthOps must not use real personal, clinical, financial, employment or organisational records.

All generated data should be fictional.

When contributing, do not add:

- real resident, patient, staff or provider records
- real NHS numbers or health identifiers
- real addresses linked to individuals
- real phone numbers or emails belonging to individuals
- real financial account details
- real employment records
- real safeguarding records
- real clinical records
- real commercially confidential datasets

Synthetic assumptions should be documented clearly and should not be presented as official benchmarks or real-world statistics.

---

## Development Setup

Clone the repository:

```powershell
git clone https://github.com/Phoenix-maho/synthops.git
cd synthops
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project in editable mode with development dependencies:

```powershell
pip install -e ".[dev]"
```

Run the tests:

```powershell
pytest
```

---

## Branching Workflow

Create a new branch for each meaningful change.

Use descriptive branch names, such as:

```text
feature/resident-care-needs-history
docs/update-data-dictionary
test/care-home-validation
fix/custom-id-format
ci/add-test-workflow
```

Example:

```powershell
git checkout -b feature/resident-care-needs-history
```

Avoid making feature changes directly on `main`.

---

## Commit Guidelines

Use clear commit messages that describe the change.

Good examples:

```text
Add resident care needs history generator
Document adult social care data dictionary
Fix custom ID width validation
Add tests for resident lifecycle rules
```

Avoid vague commit messages such as:

```text
update
fix stuff
changes
work
```

A good commit should represent one meaningful unit of work.

---

## Pull Request Guidelines

Before opening a pull request:

- make sure tests pass
- update documentation if behaviour changed
- add tests for new generator logic
- keep changes focused
- explain the purpose of the change
- mention assumptions introduced or changed
- link the relevant issue using a closing keyword where appropriate

A good pull request should answer:

1. What changed?
2. Why was the change needed?
3. How was it tested?
4. Are there any limitations or assumptions?

Example closing keyword:

```text
Closes #12
```

Make sure closing keywords are outside code blocks so GitHub can detect them.

---

## Adding a New Domain Module

New domain modules should follow the existing structure:

```text
src/synthops/domains/new_domain/
├── __init__.py
├── table_generator.py
└── generate.py
```

Each domain should include:

- source code
- tests
- documentation
- sample output
- example usage
- documented assumptions
- relevant data dictionary updates

Domain-specific logic should stay inside the domain module.

Reusable logic should go into:

```text
src/synthops/core/
```

---

## Adding a New Generator Table

When adding a new table generator, include:

- generator function
- configurable ID prefix and width where relevant
- random seed support
- realistic value ranges
- referential integrity rules
- validation or tests for key assumptions
- sample output where appropriate
- documentation updates
- changelog entry

Example expected pattern:

```python
def generate_example_table(
    number_of_rows: int = 10,
    id_prefix: str = "EX",
    id_width: int = 4,
    seed: int | None = None,
):
    ...
```

---

## Testing Expectations

All important generator behaviour should be tested.

Tests should cover:

- expected output type
- expected row counts
- expected columns
- unique IDs
- custom ID formats
- invalid inputs
- valid value ranges
- date consistency
- referential integrity
- reproducibility when using seeds

Run tests with:

```powershell
pytest
```

GitHub Actions also runs the test suite automatically on pull requests and pushes to `main`.

---

## Documentation Expectations

Documentation should be updated when:

- a new feature is added
- a new domain module is introduced
- a generated table changes
- assumptions change
- responsible-use guidance changes
- setup or installation steps change
- sample outputs change

Documentation should be clear enough for:

- analysts
- analytics engineers
- BI developers
- data scientists
- open-source contributors
- technical reviewers

---

## Code Style

Current style expectations:

- write clear, readable Python
- prefer descriptive function and variable names
- keep domain assumptions visible
- avoid unnecessary cleverness
- separate reusable core logic from domain-specific logic
- include docstrings for public generator functions
- keep functions focused and testable

More formal linting and formatting tools may be added later.

---

## Reporting Issues

When reporting an issue, include:

- what you expected to happen
- what actually happened
- steps to reproduce the issue
- your operating system
- Python version
- relevant error messages
- example input if applicable

---

## Suggesting New Features

Feature suggestions should explain:

- the problem being solved
- who would benefit
- the proposed behaviour
- any relevant domain assumptions
- whether it belongs in the core engine or a domain module

For new domain suggestions, explain why that domain would benefit from synthetic operational data.

---

## Maintainer Notes

SynthOps is being developed as a professional open-source product.

Changes should improve at least one of the following:

- usefulness
- reliability
- realism
- maintainability
- documentation
- developer experience
- test coverage
- responsible data practice
- community adoption

The goal is not simply to add more generated tables. The goal is to build a trustworthy synthetic data product that others can understand, use and extend.