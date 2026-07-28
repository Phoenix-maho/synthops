# Adult Social Care Domain Module

## Overview

The Adult Social Care module is the first domain module in SynthOps.

It generates fictional but structured adult social care operations data for analytics, dashboarding, AI prototyping and decision-intelligence use cases.

The module is designed to avoid real personal data while still reflecting realistic operational patterns found in adult social care environments.

## Version 1 Tables

The first version of the module will generate:

- care homes
- residents
- staff
- shifts
- care plans
- observations
- incidents
- handover notes

## Current Table: care_homes

The `care_homes` table represents fictional adult social care provider sites.

### Columns

| Column | Description |
|---|---|
| `care_home_id` | Unique synthetic identifier for each care home |
| `care_home_name` | Fictional care home name |
| `region` | UK region |
| `local_authority` | Local authority linked to the selected region |
| `care_home_type` | Type of care home, such as Residential, Nursing, Dementia or Specialist Care |
| `turnover_profile` | Synthetic operational turnover profile used to support resident lifecycle generation |
| `bed_capacity` | Number of available beds |
| `occupancy_rate` | Synthetic occupancy rate influenced by care home type |
| `current_residents` | Estimated current residents based on bed capacity and occupancy |
| `cqc_rating` | Fictional quality-rating-style category |
| `opened_date` | Fictional opening date |

### Scenario Controls

The care home generator supports configurable scenario inputs.

Example:

```python
generate_care_homes(
    number_of_homes=1,
    care_home_type="Dementia",
    turnover_profile="High",
    id_prefix="HM",
    id_width=3,
    seed=42,
)

## Configurable ID Format

The care home generator supports configurable ID formats.

Example:

```python
generate_care_homes(
    number_of_homes=10,
    id_prefix="HM",
    id_width=3,
    seed=42,
)