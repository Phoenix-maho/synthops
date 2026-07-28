# SynthOps

**Synthetic Operational Data Generator for Analytics, AI Prototyping and Decision Intelligence**

SynthOps is an open-source synthetic data generation framework designed to create realistic, structured operational datasets across different industries.

The project helps analysts, analytics engineers, BI developers, data scientists, educators and product builders generate safe fictional datasets for dashboarding, data modelling, AI prototyping and decision-intelligence use cases.

---

## Project Status

SynthOps is currently in early development.

Version 1 starts with an **Adult Social Care** domain module and will later expand into other operational domains such as finance operations, construction operations, SaaS metrics and workforce analytics.

---

## Why This Project Exists

Realistic operational datasets are often difficult to access because they may contain sensitive, private or commercially confidential information.

This creates a barrier for people who want to practise analytics engineering, build dashboards, test AI prototypes, or demonstrate decision-support systems using realistic data.

SynthOps addresses this by generating fictional but structured datasets that reflect plausible operational patterns without using real personal or confidential data.

---

## Current Domain Module

### Adult Social Care

The first module generates synthetic adult social care operations data.

Current table:

- `care_homes`

Planned tables:

- `residents`
- `resident_care_needs_history`
- `staff`
- `shifts`
- `incidents`
- `observations`
- `handover_notes`

---

## Current Features

- Modular Python package structure
- Reusable core ID generation utilities
- Reusable date utilities
- Scenario-driven adult social care home generation
- Configurable ID prefixes and widths
- Configurable care home type
- Configurable turnover profile
- Type-influenced occupancy behaviour
- Synthetic sample CSV output
- Automated tests with `pytest`

---

## Example Usage

```python
from synthops.domains.adult_social_care.care_homes import generate_care_homes

care_homes = generate_care_homes(
    number_of_homes=10,
    care_home_type="Dementia",
    turnover_profile="High",
    id_prefix="HM",
    id_width=3,
    seed=42,
)

print(care_homes.head())
```

---

## Example Output

The current generator can create synthetic care home records with fields such as:

- `care_home_id`
- `care_home_name`
- `region`
- `local_authority`
- `care_home_type`
- `turnover_profile`
- `bed_capacity`
- `occupancy_rate`
- `current_residents`
- `cqc_rating`
- `opened_date`

---

## Project Structure

```text
synthops/
├── data/
│   └── sample/
├── docs/
├── examples/
├── notebooks/
├── src/
│   └── synthops/
│       ├── core/
│       └── domains/
├── tests/
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

## Installation for Local Development

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project in editable mode:

```powershell
pip install -e ".[dev]"
```

Run tests:

```powershell
pytest
```

---

## Generate Sample Data

Run the example script:

```powershell
python examples/generate_adult_social_care_sample.py
```

This creates a sample CSV file at:

```text
data/sample/adult_social_care/care_homes.csv
```

---

## Responsible Use

SynthOps generates fictional data for learning, analytics development, dashboarding and prototyping.

The generated data must not be used for clinical decision-making, safeguarding decisions, regulatory reporting, financial decisions, employment decisions, or real-world assessment of individuals or organisations.

The assumptions used in this project are synthetic modelling choices designed to create plausible variation for analytics and prototyping. They should not be interpreted as real-world benchmarks.

---

## Roadmap

Planned development areas include:

- Resident lifecycle generation
- Care needs history generation
- Staff and shift generation
- Incident and observation generation
- Power BI demo dashboard
- Finance operations domain module
- Construction operations domain module
- Documentation site
- Optional Streamlit interface

---

## Portfolio Purpose

This project demonstrates the design of a reusable synthetic data product with modular architecture, responsible data assumptions, test coverage, documentation and analytics-ready output.

It supports professional positioning as an Analytics Engineer / Data Scientist focused on building trusted data products that transform fragmented operational data into reliable business decisions.