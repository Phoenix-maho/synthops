"""
Synthetic care home generation for the Adult Social Care domain.

This module creates fictional care home records that can be used as the
foundation for related residents, staff, shifts, incidents and observations.
"""

from random import Random

import pandas as pd
from faker import Faker

from synthops.core.dates import random_date_between
from synthops.core.ids import generate_ids


CARE_HOME_TYPES = [
    "Residential",
    "Nursing",
    "Dementia",
    "Residential and Nursing",
    "Specialist Care",
]

CQC_RATINGS = [
    "Outstanding",
    "Good",
    "Requires Improvement",
    "Inadequate",
]

UK_REGIONS_AND_LOCAL_AUTHORITIES = {
    "South West": ["Gloucestershire", "Bristol", "Somerset", "Wiltshire"],
    "West Midlands": ["Birmingham", "Coventry", "Worcestershire", "Warwickshire"],
    "South East": ["Oxfordshire", "Berkshire", "Hampshire", "Surrey"],
    "North West": ["Manchester", "Liverpool", "Lancashire", "Cheshire"],
    "London": ["Camden", "Croydon", "Newham", "Ealing"],
}

CARE_HOME_NATURE_WORDS = [
    "Willow",
    "Rosewood",
    "Oakfield",
    "Meadow",
    "Silver Birch",
    "Hawthorn",
    "Cedar",
    "Brookside",
    "Maple",
    "Lavender",
    "Elmwood",
    "Ashgrove",
    "Primrose",
    "Riverside",
    "Fernbank",
]

CARE_HOME_SUFFIXES = [
    "Care Home",
    "House",
    "Lodge",
    "Manor",
    "Care Centre",
    "Residence",
]


def generate_care_home_name(fake: Faker, random_generator: Random) -> str:
    """
    Generate a fictional care home name using a hybrid naming strategy.

    The hybrid strategy combines curated care-style words with Faker-generated
    street names and surnames to increase variety while keeping names plausible.

    Args:
        fake: Faker instance used to generate fictional names.
        random_generator: Random instance for reproducible choices.

    Returns:
        A fictional care home name.
    """
    name_style = random_generator.choice(["nature", "street", "surname"])
    suffix = random_generator.choice(CARE_HOME_SUFFIXES)

    if name_style == "nature":
        prefix = random_generator.choice(CARE_HOME_NATURE_WORDS)
        return f"{prefix} {suffix}"

    if name_style == "street":
        street_name = fake.street_name()
        return f"{street_name} {suffix}"

    surname = fake.last_name()
    return f"{surname} {suffix}"


def generate_unique_care_home_name(
    fake: Faker,
    random_generator: Random,
    used_names: set[str],
    max_attempts: int = 100,
) -> str:
    """
    Generate a unique fictional care home name within a generated dataset.

    Args:
        fake: Faker instance used to generate fictional names.
        random_generator: Random instance for reproducible choices.
        used_names: Set of names already generated in the current dataset.
        max_attempts: Maximum number of attempts before failing.

    Returns:
        A unique fictional care home name.

    Raises:
        RuntimeError: If a unique name cannot be generated.
    """
    for _ in range(max_attempts):
        care_home_name = generate_care_home_name(fake, random_generator)

        if care_home_name not in used_names:
            used_names.add(care_home_name)
            return care_home_name

    raise RuntimeError("Unable to generate a unique care home name")


def generate_care_homes(
    number_of_homes: int = 5,
    id_prefix: str = "HOME",
    id_width: int = 4,
    seed: int | None = None,
) -> pd.DataFrame:

    records = []
    used_names = set()
    """
    Generate synthetic care home records.

    Args:
        number_of_homes: Number of care homes to generate.
        id_prefix: Prefix used for generated care home IDs.
        id_width: Number of digits used in generated care home IDs.
        seed: Optional random seed for reproducible output.

    Returns:
        A pandas DataFrame containing synthetic care home records.

    Raises:
        ValueError: If number_of_homes is less than 1.
    """
    if number_of_homes < 1:
        raise ValueError("number_of_homes must be greater than or equal to 1")

    fake = Faker("en_GB")
    Faker.seed(seed)
    random_generator = Random(seed)

    care_home_ids = generate_ids(id_prefix, number_of_homes, width=id_width)
    records = []
    used_names = set()

    for care_home_id in care_home_ids:
        region = random_generator.choice(list(UK_REGIONS_AND_LOCAL_AUTHORITIES.keys()))
        local_authority = random_generator.choice(UK_REGIONS_AND_LOCAL_AUTHORITIES[region])
        bed_capacity = random_generator.randint(20, 90)
        occupancy_rate = round(random_generator.uniform(0.72, 0.98), 2)
        current_residents = round(bed_capacity * occupancy_rate)

        records.append(
            {
                "care_home_id": care_home_id,
                "care_home_name": generate_unique_care_home_name(
                    fake,
                    random_generator,
                    used_names,
                ),
                "region": region,
                "local_authority": local_authority,
                "care_home_type": random_generator.choice(CARE_HOME_TYPES),
                "bed_capacity": bed_capacity,
                "occupancy_rate": occupancy_rate,
                "current_residents": current_residents,
                "cqc_rating": random_generator.choices(
                    CQC_RATINGS,
                    weights=[0.08, 0.72, 0.17, 0.03],
                    k=1,
                )[0],
                "opened_date": random_date_between(
                    "1985-01-01",
                    "2022-12-31",
                    seed=random_generator.randint(1, 1_000_000),
                ),
            }
        )

    return pd.DataFrame(records)