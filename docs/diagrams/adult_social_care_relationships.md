# Adult Social Care Table Relationship Diagram

This diagram shows the current and planned table relationships for the Adult Social Care domain module.

```mermaid
erDiagram
    CARE_HOMES ||--o{ RESIDENTS : has
    RESIDENTS ||--o{ RESIDENT_CARE_NEEDS_HISTORY : will_have
    CARE_HOMES ||--o{ STAFF : will_have
    CARE_HOMES ||--o{ SHIFTS : will_have
    STAFF ||--o{ SHIFTS : will_work
    RESIDENTS ||--o{ INCIDENTS : will_have
    CARE_HOMES ||--o{ INCIDENTS : will_record
    RESIDENTS ||--o{ OBSERVATIONS : will_have
    CARE_HOMES ||--o{ HANDOVER_NOTES : will_have

    CARE_HOMES {
        string care_home_id PK
        string care_home_name
        string region
        string local_authority
        string care_home_type
        string turnover_profile
        int bed_capacity
        float occupancy_rate
        int current_residents
        string cqc_rating
        date opened_date
    }

    RESIDENTS {
        string resident_id PK
        string care_home_id FK
        date date_of_birth
        string gender
        date admission_date
        date exit_date
        string exit_reason
        string status_at_dataset_end
    }

    RESIDENT_CARE_NEEDS_HISTORY {
        string care_needs_assessment_id PK
        string resident_id FK
        date assessment_date
        string dependency_level
        string mobility_support_level
        string personal_care_support_level
        string dementia_support
        string nutrition_risk
        string falls_risk
        string review_reason
    }

    STAFF {
        string staff_id PK
        string care_home_id FK
    }

    SHIFTS {
        string shift_id PK
        string care_home_id FK
        string staff_id FK
    }

    INCIDENTS {
        string incident_id PK
        string resident_id FK
        string care_home_id FK
    }

    OBSERVATIONS {
        string observation_id PK
        string resident_id FK
    }

    HANDOVER_NOTES {
        string handover_note_id PK
        string care_home_id FK
    }
```

## Implemented Tables

- `care_homes`
- `residents`

## Planned Tables

- `resident_care_needs_history`
- `staff`
- `shifts`
- `incidents`
- `observations`
- `handover_notes`

## Notes

Only `care_homes` and `residents` are currently implemented.

Planned tables are shown to explain the intended direction of the Adult Social Care module. They should not be described as implemented until the relevant generators, tests, documentation and sample outputs exist.