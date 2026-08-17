from datetime import date

import pandas as pd
import pytest

from synthops.domains.adult_social_care.care_homes import generate_care_homes
from synthops.domains.adult_social_care.residents import generate_residents


def test_generate_residents_returns_dataframe():
    care_homes = generate_care_homes(number_of_homes=2, seed=42)

    residents = generate_residents(care_homes, seed=42)

    assert isinstance(residents, pd.DataFrame)


def test_generate_residents_contains_expected_columns():
    care_homes = generate_care_homes(number_of_homes=1, seed=42)

    residents = generate_residents(care_homes, seed=42)

    expected_columns = {
        "resident_id",
        "care_home_id",
        "date_of_birth",
        "gender",
        "admission_date",
        "exit_date",
        "exit_reason",
        "status_at_dataset_end",
    }

    assert expected_columns.issubset(residents.columns)


def test_resident_ids_are_unique():
    care_homes = generate_care_homes(number_of_homes=3, seed=42)

    residents = generate_residents(care_homes, seed=42)

    assert residents["resident_id"].is_unique


def test_all_residents_link_to_valid_care_homes():
    care_homes = generate_care_homes(number_of_homes=3, seed=42)

    residents = generate_residents(care_homes, seed=42)

    valid_care_home_ids = set(care_homes["care_home_id"])

    assert set(residents["care_home_id"]).issubset(valid_care_home_ids)


def test_active_resident_count_matches_current_residents():
    care_homes = generate_care_homes(number_of_homes=3, seed=42)

    residents = generate_residents(care_homes, seed=42)

    active_residents = residents[residents["status_at_dataset_end"] == "Active"]

    actual_counts = active_residents.groupby("care_home_id").size().to_dict()
    expected_counts = care_homes.set_index("care_home_id")["current_residents"].to_dict()

    assert actual_counts == expected_counts


def test_active_residents_have_no_exit_date_or_exit_reason():
    care_homes = generate_care_homes(number_of_homes=2, seed=42)

    residents = generate_residents(care_homes, seed=42)

    active_residents = residents[residents["status_at_dataset_end"] == "Active"]

    assert active_residents["exit_date"].isna().all()
    assert active_residents["exit_reason"].isna().all()


def test_inactive_residents_have_exit_date_and_exit_reason():
    care_homes = generate_care_homes(
        number_of_homes=1,
        turnover_profile="High",
        seed=42,
    )

    residents = generate_residents(
        care_homes,
        dataset_start_date="2020-01-01",
        dataset_end_date="2024-12-31",
        seed=42,
    )

    inactive_residents = residents[
        residents["status_at_dataset_end"].isin(["Discharged", "Deceased"])
    ]

    assert not inactive_residents.empty
    assert inactive_residents["exit_date"].notna().all()
    assert inactive_residents["exit_reason"].notna().all()


def test_exit_date_is_after_admission_date_for_inactive_residents():
    care_homes = generate_care_homes(
        number_of_homes=1,
        turnover_profile="High",
        seed=42,
    )

    residents = generate_residents(
        care_homes,
        dataset_start_date="2020-01-01",
        dataset_end_date="2024-12-31",
        seed=42,
    )

    inactive_residents = residents[
        residents["status_at_dataset_end"].isin(["Discharged", "Deceased"])
    ]

    assert (
        inactive_residents["exit_date"] > inactive_residents["admission_date"]
    ).all()


def test_exit_date_is_on_or_before_dataset_end_date():
    care_homes = generate_care_homes(
        number_of_homes=1,
        turnover_profile="High",
        seed=42,
    )

    dataset_end_date = date(2024, 12, 31)

    residents = generate_residents(
        care_homes,
        dataset_start_date="2020-01-01",
        dataset_end_date=dataset_end_date,
        seed=42,
    )

    inactive_residents = residents[
        residents["status_at_dataset_end"].isin(["Discharged", "Deceased"])
    ]

    assert (inactive_residents["exit_date"] <= dataset_end_date).all()


def test_admission_date_is_on_or_before_dataset_end_date():
    care_homes = generate_care_homes(number_of_homes=2, seed=42)

    dataset_end_date = date(2024, 12, 31)

    residents = generate_residents(
        care_homes,
        dataset_end_date=dataset_end_date,
        seed=42,
    )

    assert (residents["admission_date"] <= dataset_end_date).all()


def test_date_of_birth_is_before_admission_date():
    care_homes = generate_care_homes(number_of_homes=2, seed=42)

    residents = generate_residents(care_homes, seed=42)

    assert (residents["date_of_birth"] < residents["admission_date"]).all()


def test_residents_are_adults_at_admission():
    care_homes = generate_care_homes(number_of_homes=2, seed=42)

    residents = generate_residents(care_homes, seed=42)

    age_at_admission_days = residents.apply(
        lambda row: (row["admission_date"] - row["date_of_birth"]).days,
        axis=1,
    )

    assert (age_at_admission_days >= 18 * 365).all()


def test_resident_stays_overlap_dataset_period():
    care_homes = generate_care_homes(
        number_of_homes=2,
        turnover_profile="High",
        seed=42,
    )

    dataset_start_date = date(2020, 1, 1)
    dataset_end_date = date(2024, 12, 31)

    residents = generate_residents(
        care_homes,
        dataset_start_date=dataset_start_date,
        dataset_end_date=dataset_end_date,
        seed=42,
    )

    effective_exit_date = residents["exit_date"].fillna(dataset_end_date)

    assert (residents["admission_date"] <= dataset_end_date).all()
    assert (effective_exit_date >= dataset_start_date).all()


def test_generate_residents_supports_custom_id_format():
    care_homes = generate_care_homes(number_of_homes=1, seed=42)

    residents = generate_residents(
        care_homes,
        id_prefix="R",
        id_width=3,
        seed=42,
    )

    assert residents["resident_id"].iloc[0] == "R001"


def test_generate_residents_rejects_invalid_dataset_period():
    care_homes = generate_care_homes(number_of_homes=1, seed=42)

    with pytest.raises(ValueError):
        generate_residents(
            care_homes,
            dataset_start_date="2024-12-31",
            dataset_end_date="2024-01-01",
            seed=42,
        )


def test_generate_residents_rejects_missing_required_care_home_columns():
    care_homes = pd.DataFrame(
        {
            "care_home_id": ["HOME0001"],
            "current_residents": [10],
        }
    )

    with pytest.raises(ValueError):
        generate_residents(care_homes, seed=42)


def test_high_turnover_generates_at_least_as_many_historical_residents_as_stable_turnover():
    stable_care_home = generate_care_homes(
        number_of_homes=1,
        care_home_type="Residential",
        turnover_profile="Stable",
        seed=42,
    )

    high_care_home = stable_care_home.copy()
    high_care_home["turnover_profile"] = "High"

    stable_residents = generate_residents(
        stable_care_home,
        dataset_start_date="2020-01-01",
        dataset_end_date="2024-12-31",
        seed=42,
    )

    high_residents = generate_residents(
        high_care_home,
        dataset_start_date="2020-01-01",
        dataset_end_date="2024-12-31",
        seed=42,
    )

    stable_historical_count = (
        stable_residents["status_at_dataset_end"] != "Active"
    ).sum()

    high_historical_count = (
        high_residents["status_at_dataset_end"] != "Active"
    ).sum()

    assert high_historical_count >= stable_historical_count