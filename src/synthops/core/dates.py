"""
Reusable date utilities for SynthOps.

This module contains helper functions for generating date ranges and random dates.
The functions are domain-neutral, so they can be reused across care, finance,
construction, SaaS and other future modules.
"""

from datetime import date, datetime, timedelta
from random import Random


def parse_date(value: str | date) -> date:
    """
    Convert a string or date value into a date object.

    Args:
        value: A date object or a string in YYYY-MM-DD format.

    Returns:
        A Python date object.

    Raises:
        ValueError: If the string is not in YYYY-MM-DD format.
        TypeError: If the value is not a string or date.
    """
    if isinstance(value, date):
        return value

    if isinstance(value, str):
        return datetime.strptime(value, "%Y-%m-%d").date()

    raise TypeError("value must be a date object or a string in YYYY-MM-DD format")


def generate_date_range(start_date: str | date, end_date: str | date) -> list[date]:
    """
    Generate a list of dates between start_date and end_date, inclusive.

    Example:
        generate_date_range("2026-01-01", "2026-01-03")
        returns [date(2026, 1, 1), date(2026, 1, 2), date(2026, 1, 3)]

    Args:
        start_date: Start date as a date object or YYYY-MM-DD string.
        end_date: End date as a date object or YYYY-MM-DD string.

    Returns:
        A list of date objects.

    Raises:
        ValueError: If end_date is earlier than start_date.
    """
    start = parse_date(start_date)
    end = parse_date(end_date)

    if end < start:
        raise ValueError("end_date cannot be earlier than start_date")

    number_of_days = (end - start).days

    return [start + timedelta(days=offset) for offset in range(number_of_days + 1)]


def random_date_between(
    start_date: str | date,
    end_date: str | date,
    seed: int | None = None,
) -> date:
    """
    Generate one random date between start_date and end_date, inclusive.

    Args:
        start_date: Start date as a date object or YYYY-MM-DD string.
        end_date: End date as a date object or YYYY-MM-DD string.
        seed: Optional random seed for reproducible output.

    Returns:
        A randomly selected date object.
    """
    dates = generate_date_range(start_date, end_date)
    random_generator = Random(seed)

    return random_generator.choice(dates)