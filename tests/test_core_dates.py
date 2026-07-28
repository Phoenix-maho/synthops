from datetime import date

import pytest

from synthops.core.dates import (
    generate_date_range,
    parse_date,
    random_date_between,
)


def test_parse_date_accepts_date_object():
    input_date = date(2026, 1, 1)

    assert parse_date(input_date) == input_date


def test_parse_date_converts_string_to_date():
    assert parse_date("2026-01-01") == date(2026, 1, 1)


def test_parse_date_rejects_invalid_type():
    with pytest.raises(TypeError):
        parse_date(20260101)


def test_generate_date_range_includes_start_and_end_dates():
    result = generate_date_range("2026-01-01", "2026-01-03")

    assert result == [
        date(2026, 1, 1),
        date(2026, 1, 2),
        date(2026, 1, 3),
    ]


def test_generate_date_range_rejects_end_before_start():
    with pytest.raises(ValueError):
        generate_date_range("2026-01-05", "2026-01-01")


def test_random_date_between_returns_date_inside_range():
    result = random_date_between("2026-01-01", "2026-01-31", seed=42)

    assert date(2026, 1, 1) <= result <= date(2026, 1, 31)


def test_random_date_between_is_reproducible_with_seed():
    first_result = random_date_between("2026-01-01", "2026-01-31", seed=42)
    second_result = random_date_between("2026-01-01", "2026-01-31", seed=42)

    assert first_result == second_result