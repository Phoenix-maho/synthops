import pandas as pd
import pytest

from synthops.domains.adult_social_care.care_homes import generate_care_homes


def test_generate_care_homes_returns_dataframe():
    result = generate_care_homes(number_of_homes=3, seed=42)

    assert isinstance(result, pd.DataFrame)


def test_generate_care_homes_returns_expected_number_of_rows():
    result = generate_care_homes(number_of_homes=4, seed=42)

    assert len(result) == 4


def test_generate_care_homes_contains_expected_columns():
    result = generate_care_homes(number_of_homes=2, seed=42)

    expected_columns = [
        "care_home_id",
        "care_home_name",
        "region",
        "local_authority",
        "care_home_type",
        "turnover_profile",
        "bed_capacity",
        "occupancy_rate",
        "current_residents",
        "cqc_rating",
        "opened_date",
    ]

    assert list(result.columns) == expected_columns


def test_generate_care_homes_ids_are_unique():
    result = generate_care_homes(number_of_homes=10, seed=42)

    assert result["care_home_id"].is_unique


def test_generate_care_homes_rejects_invalid_number_of_homes():
    with pytest.raises(ValueError):
        generate_care_homes(number_of_homes=0)


def test_current_residents_do_not_exceed_bed_capacity():
    result = generate_care_homes(number_of_homes=20, seed=42)

    assert (result["current_residents"] <= result["bed_capacity"]).all()


def test_occupancy_rate_is_between_global_expected_bounds():
    result = generate_care_homes(number_of_homes=20, seed=42)

    assert (result["occupancy_rate"] >= 0.65).all()
    assert (result["occupancy_rate"] <= 0.99).all()


def test_generate_care_homes_supports_custom_id_format():
    result = generate_care_homes(
        number_of_homes=3,
        id_prefix="HM",
        id_width=3,
        seed=42,
    )

    assert result["care_home_id"].tolist() == ["HM001", "HM002", "HM003"]


def test_generate_care_homes_names_are_unique():
    result = generate_care_homes(number_of_homes=10, seed=42)

    assert result["care_home_name"].is_unique


def test_generate_care_homes_supports_selected_care_home_type():
    result = generate_care_homes(
        number_of_homes=3,
        care_home_type="Dementia",
        seed=42,
    )

    assert (result["care_home_type"] == "Dementia").all()


def test_generate_care_homes_rejects_invalid_care_home_type():
    with pytest.raises(ValueError):
        generate_care_homes(
            number_of_homes=1,
            care_home_type="Hospital",
            seed=42,
        )


def test_generate_care_homes_supports_selected_turnover_profile():
    result = generate_care_homes(
        number_of_homes=3,
        turnover_profile="High",
        seed=42,
    )

    assert (result["turnover_profile"] == "High").all()


def test_generate_care_homes_rejects_invalid_turnover_profile():
    with pytest.raises(ValueError):
        generate_care_homes(
            number_of_homes=1,
            turnover_profile="Fast",
            seed=42,
        )


def test_dementia_home_occupancy_uses_dementia_range():
    result = generate_care_homes(
        number_of_homes=10,
        care_home_type="Dementia",
        seed=42,
    )

    assert (result["occupancy_rate"] >= 0.82).all()
    assert (result["occupancy_rate"] <= 0.99).all()


def test_specialist_care_occupancy_uses_specialist_range():
    result = generate_care_homes(
        number_of_homes=10,
        care_home_type="Specialist Care",
        seed=42,
    )

    assert (result["occupancy_rate"] >= 0.65).all()
    assert (result["occupancy_rate"] <= 0.93).all()