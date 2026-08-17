# 0002: Time-Aware Resident Lifecycle Modelling

## Status

Accepted

## Date

2026-08-17

## Context

SynthOps is being developed as a synthetic operational data generation framework.

The first implemented domain is Adult Social Care. The first table in this domain is `care_homes`, which represents fictional care provider sites. The next planned table is `residents`.

A key modelling decision is required before implementing resident generation:

Should the `residents` table represent only residents who are currently active at the end of the dataset, or should it represent residents who passed through a care home during a generated time period?

This decision matters because adult social care operations are time-based. Residents are admitted, remain for different lengths of time, may be discharged, may move to another care setting, or may die. Their care needs can also change during their stay.

If SynthOps generates only a static list of current residents, the dataset may be simpler, but it will not support realistic analytics use cases such as:

- admissions and exits over time
- occupancy history
- length-of-stay analysis
- resident turnover
- care-needs progression
- incident rates during valid stay periods
- handover history
- temporal data quality checks
- point-in-time reporting

SynthOps is intended to support analytics engineering, BI, AI prototyping and decision-intelligence use cases. These use cases often require historical and time-aware data, not just static snapshots.

## Decision

SynthOps will model residents as time-aware lifecycle records.

The `residents` table will represent residents who had a valid stay in a care home during a generated dataset period.

The dataset period will be controlled by:

```text
dataset_start_date
dataset_end_date
```

A resident should be included when their stay overlaps the generated dataset period.

The residents table will store lifecycle base facts such as:

```text
resident_id
care_home_id
date_of_birth
gender
admission_date
exit_date
exit_reason
status_at_dataset_end
```

The residents table should not store derived analytics fields as primary generated facts.

For example, the table should not permanently store:

```text
current_age
age_band
age_at_admission
length_of_stay
```

These values can be derived later from base facts during analytics transformation.

The number of active residents at `dataset_end_date` should match the `current_residents` value generated for each care home.

Historical resident volume should vary based on:

- dataset length
- care home bed capacity
- turnover profile
- random variation

This means that a five-year dataset should usually contain more historical resident records than a one-year dataset, and a high-turnover care home should usually contain more historical resident movement than a stable-turnover care home.

## Alternatives Considered

### Alternative 1: Generate only active residents

This option would generate exactly one row per resident currently living in each care home at the dataset end point.

Possible advantages:

- simpler to implement
- easier to explain initially
- fewer date rules
- fewer edge cases
- easier to match current occupancy

Disadvantages:

- does not support historical analysis
- does not support admissions and exits over time
- does not support realistic resident turnover
- limits future care-needs history generation
- limits incidents, observations and handovers to a static population
- makes the dataset less useful for analytics engineering and BI practice

This option was rejected because it would make SynthOps less realistic and less useful for time-based operational analytics.

### Alternative 2: Generate residents with current status but no dataset period

This option would allow active, discharged and deceased residents, but without a clearly defined generated time window.

Possible advantages:

- supports more than active-only residents
- adds some lifecycle realism
- simpler than full time-aware modelling

Disadvantages:

- unclear what time period the dataset represents
- difficult to validate whether events belong inside the dataset
- harder to align incidents and observations to valid stay periods
- harder to reason about occupancy at a specific point in time
- could create inconsistent or confusing generated records

This option was rejected because time-aware datasets need a clear reporting window.

### Alternative 3: Use a dataset period and include residents whose stay overlaps that period

This option uses `dataset_start_date` and `dataset_end_date` to define the generated history window.

Possible advantages:

- supports realistic operational history
- supports point-in-time reporting
- supports historical resident movement
- supports occupancy and turnover analysis
- supports future care-needs history
- supports incidents and observations during valid stay periods
- creates clearer validation rules
- aligns with analytics engineering modelling practices

Disadvantages:

- more complex to implement
- requires careful date validation
- requires active resident counts to match care home occupancy
- requires thoughtful handling of admissions, exits and status

This option was accepted.

## Consequences

### Positive Consequences

This decision allows SynthOps to support more realistic analytics use cases, including:

- resident lifecycle reporting
- occupancy analysis
- admissions and exits over time
- length-of-stay calculations
- resident turnover analysis
- time-aware care-needs history
- valid incident and observation timelines
- historical dashboarding
- point-in-time reconstruction

It also supports stronger analytics engineering practice because raw generated tables store base facts and allow derived fields to be calculated later.

### Negative Consequences

This decision adds implementation complexity.

The residents generator must handle:

- valid dataset start and end dates
- admissions before the dataset start date
- admissions during the dataset period
- active residents at the dataset end date
- discharged residents
- deceased residents
- exit dates after admission dates
- exit dates within the dataset window
- matching active resident counts to care home occupancy
- ensuring resident stays overlap the dataset period

This requires more tests than a static residents table.

## Implementation Rules

The residents generator should follow these rules.

### Dataset Period Rules

- `dataset_start_date` must be on or before `dataset_end_date`.
- Residents should be generated relative to the dataset period.
- A resident should be included if their stay overlaps the dataset period.
- `admission_date` must be on or before `dataset_end_date`.

### Resident Age Rules

- `date_of_birth` must be before `admission_date`.
- Residents must be adults at admission.
- The generator should avoid unnecessary personally identifying data.
- The residents table should not include full names, addresses, phone numbers, NHS numbers or next-of-kin details in the initial version.

### Active Resident Rules

- Active residents should have `status_at_dataset_end` set to `Active`.
- Active residents should not have an `exit_date`.
- Active residents should not have an `exit_reason`.
- The number of active residents for each care home at `dataset_end_date` should match the care home's `current_residents` value.

### Inactive Resident Rules

- Inactive residents should have `status_at_dataset_end` set to either `Discharged` or `Deceased`.
- Inactive residents should have an `exit_date`.
- `exit_date` must be after `admission_date`.
- `exit_date` must be on or before `dataset_end_date`.
- `exit_reason` should align with the resident status.

### Turnover Rules

Historical resident volume should be influenced by:

- `turnover_profile`
- `bed_capacity`
- dataset length
- random variation

For example, care homes with a `High` turnover profile should usually generate more historical resident records than care homes with a `Stable` turnover profile, all else being broadly equal.

The relationship should be realistic but not deterministic.

### Derivation Rules

The raw generated residents table should store base facts.

The following should be derived later in analytics transformations:

- current age
- age band
- age at admission
- length of stay
- active flag at a chosen reporting date
- resident tenure group

This supports cleaner data modelling and avoids storing values that can become stale or inconsistent.

## Testing Requirements

The residents generator should include tests for:

- expected output type
- expected columns
- unique `resident_id`
- valid `care_home_id` references
- active resident count matching `care_homes.current_residents`
- active residents having no `exit_date`
- active residents having no `exit_reason`
- inactive residents having valid `exit_date`
- inactive residents having valid `exit_reason`
- `exit_date` after `admission_date`
- `exit_date` on or before `dataset_end_date`
- `admission_date` on or before `dataset_end_date`
- `date_of_birth` before `admission_date`
- residents being adults at admission
- generated resident stays overlapping the dataset period
- custom ID prefix and width
- reproducible output when using a seed

These tests are necessary because time-aware synthetic data can easily become internally inconsistent.

## Impact on Future Tables

This decision affects future Adult Social Care tables.

### `resident_care_needs_history`

Care-needs assessments must occur during the resident's valid stay period.

Assessment dates should be:

- on or after `admission_date`
- on or before `exit_date` for inactive residents
- on or before `dataset_end_date` for active residents

### `incidents`

Incidents must be linked to residents who were in the care home on the incident date.

### `observations`

Observations must occur during a valid resident stay period.

### `handover_notes`

Handover notes should reference valid residents, dates and care homes.

### Occupancy Reporting

Occupancy can be calculated at the dataset end date using active residents.

Future versions may support occupancy reconstruction at any date within the dataset period.

## Responsible Use

Resident lifecycle data generated by SynthOps is fictional.

Generated residents must not be treated as real people.

The generator should avoid unnecessary personal identifiers and should not attempt to model sensitive personal histories in a way that could be mistaken for real records.

Synthetic assumptions about discharge, death, length of stay or care needs should not be presented as clinical, regulatory or sector benchmarks.

## Review Trigger

This decision should be reviewed when:

- the resident generator is implemented
- care-needs history is implemented
- incident generation is implemented
- point-in-time occupancy reconstruction is added
- a second domain requires lifecycle-style modelling
- the project approaches a stable Adult Social Care release

At that point, some lifecycle logic may need to move into reusable core utilities if it proves useful across domains.

## Summary

SynthOps will model residents as time-aware lifecycle records.

The residents table will include people whose stay overlaps a generated dataset period, rather than only residents active at a single point in time.

This decision supports realistic analytics engineering, longitudinal reporting, future care-needs history, incident modelling and point-in-time operational analysis.