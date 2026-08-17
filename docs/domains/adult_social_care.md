# Adult Social Care Domain Module

## Overview

The Adult Social Care module is the first domain module in SynthOps.

It generates fictional but structured adult social care operations data for analytics engineering, business intelligence, AI prototyping and decision-intelligence use cases.

The module is designed to avoid real personal, clinical, provider or staff data while still reflecting plausible operational patterns such as care homes, resident lifecycles, care needs, staffing, incidents, observations and handovers.

Adult Social Care is treated as the first domain module, not the entire product. SynthOps is designed to expand into other operational domains such as finance operations, construction operations, SaaS metrics and workforce analytics.

---

## Current Status

The Adult Social Care module is in early development.

Current implemented table:

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

## Current Table: `care_homes`

The `care_homes` table represents fictional adult social care provider sites.

It acts as the parent table for future Adult Social Care datasets. Residents, staff, shifts, incidents, observations and handover notes will link back to care homes.

### Columns

| Column | Description |
|---|---|
| `care_home_id` | Unique synthetic identifier for each care home |
| `care_home_name` | Fictional care home name |
| `region` | UK region |
| `local_authority` | Local authority linked to the selected region |
| `care_home_type` | Type of care setting |
| `turnover_profile` | Synthetic operational turnover profile |
| `bed_capacity` | Number of available beds |
| `occupancy_rate` | Synthetic occupancy rate influenced by care home type |
| `current_residents` | Estimated number of residents active at the dataset end point |
| `cqc_rating` | Fictional quality-rating-style category |
| `opened_date` | Fictional opening date |

---

## Care Home Types

The current generator supports the following care home types:

- `Residential`
- `Nursing`
- `Dementia`
- `Residential and Nursing`
- `Specialist Care`

Care home type is a scenario driver. It is not just a descriptive label.

It influences:

- occupancy behaviour
- turnover profile selection
- future resident population patterns
- future dependency and care-needs assumptions
- future incident and observation patterns

For example, a dementia care setting may later generate a different care-needs profile from a general residential care setting.

---

## Turnover Profiles

The current generator supports the following turnover profiles:

- `Stable`
- `Moderate`
- `High`
- `Variable`

Turnover profile is used to describe expected resident movement over time.

In future resident lifecycle generation, turnover profile will influence how many residents pass through a care home during a generated dataset period.

For example:

| Turnover Profile | Intended Meaning |
|---|---|
| `Stable` | Lower resident movement over time |
| `Moderate` | Typical resident movement |
| `High` | Higher resident movement |
| `Variable` | Wider and less predictable resident movement |

These are synthetic modelling assumptions. They are not real-world sector benchmarks.

---

## Scenario Controls

The care home generator supports configurable scenario inputs.

Example:

```python
from synthops.domains.adult_social_care.care_homes import generate_care_homes

care_homes = generate_care_homes(
    number_of_homes=1,
    care_home_type="Dementia",
    turnover_profile="High",
    id_prefix="HM",
    id_width=3,
    seed=42,
)
```

This allows users to generate a specific scenario, such as one high-turnover dementia care home.

Users can also generate a mixed portfolio:

```python
care_homes = generate_care_homes(
    number_of_homes=10,
    id_prefix="HM",
    id_width=3,
    seed=42,
)
```

When `care_home_type` is not specified, the generator creates a mix of supported care home types.

When `turnover_profile` is not specified, the generator selects a turnover profile based on the selected care home type.

---

## Synthetic Care Home Type Assumptions

The current generator uses care home type profiles to create plausible variation.

| Care Home Type | Occupancy Behaviour | Turnover Behaviour |
|---|---|---|
| `Residential` | Moderate occupancy | Stable to moderate turnover |
| `Nursing` | Moderate to high occupancy | Moderate to high turnover |
| `Dementia` | Higher occupancy tendency | Moderate to high turnover |
| `Residential and Nursing` | Moderate to high occupancy | Moderate turnover |
| `Specialist Care` | Wider occupancy variation | Stable, moderate, high or variable turnover |

These assumptions are used to create useful synthetic variation for analytics and prototyping.

They should not be interpreted as official statistics, operational benchmarks or evidence about real care providers.

---

## Synthetic Data Rules

The current `care_homes` generator applies these rules:

- care home IDs must be unique
- care home names must be unique within a generated dataset
- users can customise ID prefix and ID width
- care home type must be one of the supported values
- turnover profile must be one of the supported values
- care home type influences occupancy range
- turnover profile is selected based on care home type unless specified by the user
- bed capacity must be realistic for a care setting
- current residents must not exceed bed capacity
- local authority must belong to the selected region
- generated care home names must be fictional
- generated data must not represent real providers

---

## Planned Table: `residents`

The planned `residents` table will represent resident lifecycle records.

It should not represent only residents active at a single point in time.

Instead, it should represent residents who passed through a care home during a generated dataset period.

Planned columns:

| Column | Description |
|---|---|
| `resident_id` | Unique synthetic resident identifier |
| `care_home_id` | Linked care home |
| `date_of_birth` | Synthetic date of birth used for age derivation |
| `gender` | Synthetic demographic attribute |
| `admission_date` | Date resident entered the care home |
| `exit_date` | Date resident left the care home, if applicable |
| `exit_reason` | Reason for leaving, if applicable |
| `status_at_dataset_end` | Resident status at the end of the generated dataset period |

The residents table will avoid unnecessary personal identifiers such as full names, addresses, phone numbers, NHS numbers or next-of-kin details.

---

## Planned Table: `resident_care_needs_history`

The planned `resident_care_needs_history` table will represent changing care needs over time.

Care needs should not be treated as permanent resident attributes.

Planned columns:

| Column | Description |
|---|---|
| `care_needs_assessment_id` | Unique synthetic assessment identifier |
| `resident_id` | Linked resident |
| `assessment_date` | Date of care-needs assessment |
| `dependency_level` | Synthetic dependency level |
| `mobility_support_level` | Synthetic mobility support need |
| `personal_care_support_level` | Synthetic personal care support need |
| `dementia_support` | Synthetic dementia support indicator |
| `nutrition_risk` | Synthetic nutrition risk level |
| `falls_risk` | Synthetic falls risk level |
| `review_reason` | Reason the assessment was generated |

Future care-needs history should support realistic patterns such as changing support needs over time and possible deterioration before exit or death, while avoiding claims of clinical prediction.

---

## Time-Aware Modelling Principles

The Adult Social Care module should support historical datasets.

Future generators should use:

- `dataset_start_date`
- `dataset_end_date`

These dates define the generated history window.

This allows SynthOps to represent:

- residents already admitted before the dataset start date
- residents admitted during the dataset period
- residents active at the dataset end date
- residents discharged during the dataset period
- residents who died during the dataset period
- changing care needs over time
- incidents and observations linked to valid resident stay periods

This is more realistic than generating a static one-day snapshot.

---

## Resident Lifecycle Rules

Future resident generation should follow these rules:

- every resident must link to a valid care home
- `date_of_birth` must be before `admission_date`
- residents must be adults at admission
- `admission_date` must be on or before `dataset_end_date`
- active residents should have no `exit_date`
- discharged or deceased residents should have an `exit_date`
- `exit_date` must be after `admission_date`
- `exit_date` must be on or before `dataset_end_date`
- each care home's active resident count at `dataset_end_date` should match `current_residents`
- historical resident volume should vary by care home and turnover profile

---

## Care Needs History Rules

Future care-needs history generation should follow these rules:

- every care-needs record must link to a valid resident
- assessment dates must fall within the resident's stay period
- care needs should be able to change over time
- longer resident stays may have more assessments
- care-needs progression should be plausible but not deterministic
- deterioration patterns may be generated for some residents before death
- generated risks must not be presented as clinical predictions

---

## Responsible Use

This domain module generates fictional synthetic data for learning, analytics development, dashboarding and prototyping.

It must not be used for:

- clinical decision-making
- safeguarding decisions
- regulatory reporting
- inspection judgements
- real-world care-quality assessment
- real-world evaluation of individuals, providers or organisations

Generated data must not be presented as real care data.

Synthetic assumptions must not be presented as official sector statistics.

---

## Current Limitations

The Adult Social Care module is still in early development.

Current limitations:

- only `care_homes` is implemented
- resident lifecycle generation is not implemented yet
- care-needs history is not implemented yet
- staff, shifts, incidents, observations and handovers are planned but not implemented
- assumptions are synthetic and not sector benchmarks
- no dashboard-ready full dataset exists yet

These limitations will be addressed through the project roadmap.