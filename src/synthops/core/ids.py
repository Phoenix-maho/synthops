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

    Args:
        prefix: Short text prefix describing the entity type.
        number: The numeric part of the ID.
        width: Number of digits to pad the number to.

    Returns:
        A formatted synthetic ID string.
    """
    if not prefix:
        raise ValueError("prefix cannot be empty")

    if number < 1:
        raise ValueError("number must be greater than or equal to 1")

    return f"{prefix.upper()}{number:0{width}d}"


def generate_ids(prefix: str, count: int, width: int = 4) -> list[str]:
    """
    Generate a list of readable synthetic IDs.

    Example:
        generate_ids("STAFF", 3) returns ["STAFF0001", "STAFF0002", "STAFF0003"]

    Args:
        prefix: Short text prefix describing the entity type.
        count: Number of IDs to generate.
        width: Number of digits to pad the number to.

    Returns:
        A list of formatted synthetic ID strings.
    """
    if count < 1:
        raise ValueError("count must be greater than or equal to 1")

    return [generate_id(prefix, number, width) for number in range(1, count + 1)]