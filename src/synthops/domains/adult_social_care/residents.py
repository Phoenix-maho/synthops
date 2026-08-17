from __future__ import annotations

import random
from datetime import date, timedelta

import pandas as pd

from synthops.core.dates import parse_date, random_date_between
from synthops.core.ids import generate_ids


VALID_STATUSES = ["Active", "Discharged", "Deceased"]

VALID_EXIT_REASONS = {
    "Discharged": [
        "Returned home",
        "Moved to another care setting",
        "Family decision",
        "Care needs changed",
    ],
    "Deceased": [
        "Deceased",
    ],
}

GENDERS = ["Female", "Male", "Other / Not specified"]

TURNOVER_RATE_RANGES = {
    "Stable": (0.08, 0.15),
    "Moderate": (0.16, 0.28),
    "High": (0.29, 0.45),
    "Variable": (0.10, 0.50),
}


def calculate_dataset_years(dataset_start_date: date, dataset_end_date: date) -> float:
    """Calculate dataset length in years."""
    days = (dataset_end_date - dataset_start_date).days + 1
    return max(days / 365.25, 0)


def calculate_historical_resident_count(
    bed_capacity: int,
    turnover_profile: str,
    dataset_years: float,
    random_generator: random.Random,
) -> int:
    """Estimate historical resident volume based on capacity, turnover and dataset length."""
    if turnover_profile not in TURNOVER_RATE_RANGES:
        raise ValueError(
            f"Invalid turnover_profile '{turnover_profile}'. "
            f"Expected one of: {', '.join(TURNOVER_RATE_RANGES)}"
        )

    low_rate, high_rate = TURNOVER_RATE_RANGES[turnover_profile]
    annual_turnover_rate = random_generator.uniform(low_rate, high_rate)

    expected_count = bed_capacity * annual_turnover_rate * dataset_years
    variation_factor = random_generator.uniform(0.75, 1.25)

    return max(round(expected_count * variation_factor), 0)


def generate_date_of_birth(
    admission_date: date,
    random_generator: random.Random,
) -> date:
    """Generate a synthetic date of birth for an adult resident."""
    age_at_admission = random_generator.randint(55, 100)

    earliest_birth_year = admission_date.year - age_at_admission

    # Keep the month/day simple and valid by sampling from a safe date range.
    latest_possible_birth_date = date(
        earliest_birth_year,
        admission_date.month,
        min(admission_date.day, 28),
    )

    earliest_possible_birth_date = latest_possible_birth_date - timedelta(days=365 * 2)

    return random_date_between(
        earliest_possible_birth_date,
        latest_possible_birth_date,
        seed=random_generator.randint(1, 999_999),
    )


def generate_active_resident(
    resident_id: str,
    care_home_id: str,
    dataset_start_date: date,
    dataset_end_date: date,
    random_generator: random.Random,
) -> dict:
    """Generate one resident active at the dataset end date."""
    earliest_admission_date = dataset_start_date - timedelta(days=365 * 5)

    admission_date = random_date_between(
        earliest_admission_date,
        dataset_end_date,
        seed=random_generator.randint(1, 999_999),
    )

    return {
        "resident_id": resident_id,
        "care_home_id": care_home_id,
        "date_of_birth": generate_date_of_birth(admission_date, random_generator),
        "gender": random_generator.choices(GENDERS, weights=[0.58, 0.40, 0.02], k=1)[0],
        "admission_date": admission_date,
        "exit_date": None,
        "exit_reason": None,
        "status_at_dataset_end": "Active",
    }


def generate_inactive_resident(
    resident_id: str,
    care_home_id: str,
    dataset_start_date: date,
    dataset_end_date: date,
    random_generator: random.Random,
) -> dict:
    """Generate one discharged or deceased resident whose stay overlaps the dataset period."""
    earliest_admission_date = dataset_start_date - timedelta(days=365 * 5)

    latest_admission_date = dataset_end_date - timedelta(days=1)

    admission_date = random_date_between(
        earliest_admission_date,
        latest_admission_date,
        seed=random_generator.randint(1, 999_999),
    )

    earliest_exit_date = max(admission_date + timedelta(days=1), dataset_start_date)

    exit_date = random_date_between(
        earliest_exit_date,
        dataset_end_date,
        seed=random_generator.randint(1, 999_999),
    )

    status = random_generator.choices(
        ["Discharged", "Deceased"],
        weights=[0.72, 0.28],
        k=1,
    )[0]

    exit_reason = random_generator.choice(VALID_EXIT_REASONS[status])

    return {
        "resident_id": resident_id,
        "care_home_id": care_home_id,
        "date_of_birth": generate_date_of_birth(admission_date, random_generator),
        "gender": random_generator.choices(GENDERS, weights=[0.58, 0.40, 0.02], k=1)[0],
        "admission_date": admission_date,
        "exit_date": exit_date,
        "exit_reason": exit_reason,
        "status_at_dataset_end": status,
    }


def validate_care_homes_input(care_homes: pd.DataFrame) -> None:
    """Validate that the care homes DataFrame contains required resident-generation fields."""
    required_columns = {
        "care_home_id",
        "current_residents",
        "bed_capacity",
        "turnover_profile",
    }

    missing_columns = required_columns.difference(care_homes.columns)

    if missing_columns:
        raise ValueError(
            "care_homes is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )


def generate_residents(
    care_homes: pd.DataFrame,
    dataset_start_date: str | date = "2024-01-01",
    dataset_end_date: str | date = "2024-12-31",
    id_prefix: str = "RES",
    id_width: int = 5,
    seed: int | None = None,
) -> pd.DataFrame:
    """
    Generate synthetic resident lifecycle records for Adult Social Care.

    The generated residents table includes residents whose stay overlaps the
    generated dataset period. Active resident counts at dataset_end_date match
    each care home's current_residents value.

    Parameters
    ----------
    care_homes:
        DataFrame generated by the Adult Social Care care_homes generator.
    dataset_start_date:
        Start date of the generated dataset period.
    dataset_end_date:
        End date of the generated dataset period.
    id_prefix:
        Prefix used for generated resident IDs.
    id_width:
        Numeric width used for generated resident IDs.
    seed:
        Optional random seed for reproducible output.

    Returns
    -------
    pandas.DataFrame
        Synthetic resident lifecycle records.
    """
    validate_care_homes_input(care_homes)

    parsed_start_date = parse_date(dataset_start_date)
    parsed_end_date = parse_date(dataset_end_date)

    if parsed_start_date > parsed_end_date:
        raise ValueError("dataset_start_date must be on or before dataset_end_date.")

    random_generator = random.Random(seed)
    dataset_years = calculate_dataset_years(parsed_start_date, parsed_end_date)

    resident_rows: list[dict] = []

    total_active_residents = int(care_homes["current_residents"].sum())

    total_historical_residents = 0
    historical_counts_by_home: dict[str, int] = {}

    for care_home in care_homes.to_dict("records"):
        historical_count = calculate_historical_resident_count(
            bed_capacity=int(care_home["bed_capacity"]),
            turnover_profile=str(care_home["turnover_profile"]),
            dataset_years=dataset_years,
            random_generator=random_generator,
        )
        historical_counts_by_home[str(care_home["care_home_id"])] = historical_count
        total_historical_residents += historical_count

    total_residents = total_active_residents + total_historical_residents

    resident_ids = generate_ids(id_prefix, total_residents, width=id_width)
    resident_id_index = 0

    for care_home in care_homes.to_dict("records"):
        care_home_id = str(care_home["care_home_id"])
        active_count = int(care_home["current_residents"])
        historical_count = historical_counts_by_home[care_home_id]

        for _ in range(active_count):
            resident_rows.append(
                generate_active_resident(
                    resident_id=resident_ids[resident_id_index],
                    care_home_id=care_home_id,
                    dataset_start_date=parsed_start_date,
                    dataset_end_date=parsed_end_date,
                    random_generator=random_generator,
                )
            )
            resident_id_index += 1

        for _ in range(historical_count):
            resident_rows.append(
                generate_inactive_resident(
                    resident_id=resident_ids[resident_id_index],
                    care_home_id=care_home_id,
                    dataset_start_date=parsed_start_date,
                    dataset_end_date=parsed_end_date,
                    random_generator=random_generator,
                )
            )
            resident_id_index += 1

    columns = [
        "resident_id",
        "care_home_id",
        "date_of_birth",
        "gender",
        "admission_date",
        "exit_date",
        "exit_reason",
        "status_at_dataset_end",
    ]

    return pd.DataFrame(resident_rows, columns=columns)