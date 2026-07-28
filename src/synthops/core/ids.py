"""
Reusable ID generation utilities for SynthOps.

This module contains helper functions for creating readable synthetic IDs.
The goal is to keep ID formats consistent across different domain modules.
"""


def generate_id(prefix: str, number: int, width: int = 4) -> str:
    """
    Generate a readable synthetic ID.

    Example:
        generate_id("RES", 1) returns "RES0001"
        generate_id("HM", 1, width=3) returns "HM001"

    Args:
        prefix: Short text prefix describing the entity type.
        number: The numeric part of the ID.
        width: Number of digits to pad the number to.

    Returns:
        A formatted synthetic ID string.

    Raises:
        ValueError: If prefix is empty, number is less than 1, or width is less than 1.
    """
    if not prefix or not prefix.strip():
        raise ValueError("prefix cannot be empty")

    if number < 1:
        raise ValueError("number must be greater than or equal to 1")

    if width < 1:
        raise ValueError("width must be greater than or equal to 1")

    clean_prefix = prefix.strip().upper()

    return f"{clean_prefix}{number:0{width}d}"


def generate_ids(prefix: str, count: int, width: int = 4) -> list[str]:
    """
    Generate a list of readable synthetic IDs.

    Example:
        generate_ids("STAFF", 3) returns ["STAFF0001", "STAFF0002", "STAFF0003"]
        generate_ids("HM", 3, width=3) returns ["HM001", "HM002", "HM003"]

    Args:
        prefix: Short text prefix describing the entity type.
        count: Number of IDs to generate.
        width: Number of digits to pad the number to.

    Returns:
        A list of formatted synthetic ID strings.

    Raises:
        ValueError: If count is less than 1.
    """
    if count < 1:
        raise ValueError("count must be greater than or equal to 1")

    return [generate_id(prefix, number, width) for number in range(1, count + 1)]