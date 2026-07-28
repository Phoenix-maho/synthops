"""
Synthetic care home generation for the Adult Social Care domain.

This module creates fictional care home records that can be used as the
foundation for related residents, staff, shifts, incidents, observations
and care-needs history.
"""

from random import Random

import pandas as pd
from faker import Faker

from synthops.core.dates import random_date_between
from synthops.core.ids import generate_ids


CARE_HOME_TYPE_PROFILES = {
    "Residential": {
        "occupancy_range": (0.75, 0.96),
        "turnover_profiles": ["Stable", "Moderate"],
    },
    "Nursing": {
        "occupancy_range": (0.78, 0.98),
        "turnover_profiles": ["Moderate", "High"],
    },
    "Dementia": {
        "occupancy_range": (0.82, 0.99),
        "turnover_profiles": ["Moderate", "High"],
    },
    "Residential and Nursing": {
        "occupancy_range": (0.78, 0.97),
        "turnover_profiles": ["Moderate"],
    },
    "Specialist Care": {
        "occupancy_range": (0.65, 0.93),
        "turnover_profiles": ["Stable", "Moderate", "High", "Variable"],
    },
}

VALID_CARE_HOME_TYPES = list(CARE_HOME_TYPE_PROFILES.keys())

VALID_TURNOVER_PROFILES = [
    "Stable",
    "Moderate",
    "High",
    "Variable",
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


def validate_care_home_type(care_home_type: str | None) -> None:
    """
    Validate a user-supplied care home type.

    Args:
        care_home_type: Optional care home type supplied by the user.

    Raises:
        ValueError: If the care home type is not supported.
    """
    if care_home_type is None:
        return

    if care_home_type not in VALID_CARE_HOME_TYPES:
        valid_types = ", ".join(VALID_CARE_HOME_TYPES)
        raise ValueError(f"care_home_type must be one of: {valid_types}")


def validate_turnover_profile(turnover_profile: str | None) -> None:
    """
    Validate a user-supplied turnover profile.

    Args:
        turnover_profile: Optional turnover profile supplied by the user.

    Raises:
        ValueError: If the turnover profile is not supported.
    """
    if turnover_profile is None:
        return

    if turnover_profile not in VALID_TURNOVER_PROFILES:
        valid_profiles = ", ".join(VALID_TURNOVER_PROFILES)
        raise ValueError(f"turnover_profile must be one of: {valid_profiles}")


def select_care_home_type(
    random_generator: Random,
    care_home_type: str | None = None,
) -> str:
    """
    Select a care home type.

    If the user supplies a care home type, use it. Otherwise, randomly choose
    a supported care home type.

    Args:
        random_generator: Random instance for reproducible choices.
        care_home_type: Optional user-selected care home type.

    Returns:
        Selected care home type.
    """
    if care_home_type is not None:
        return care_home_type

    return random_generator.choice(VALID_CARE_HOME_TYPES)


def select_turnover_profile(
    selected_care_home_type: str,
    random_generator: Random,
    turnover_profile: str | None = None,
) -> str:
    """
    Select a turnover profile for a care home.

    If the user supplies a turnover profile, use it. Otherwise, choose one of
    the turnover profiles associated with the selected care home type.

    Args:
        selected_care_home_type: Care home type selected for the record.
        random_generator: Random instance for reproducible choices.
        turnover_profile: Optional user-selected turnover profile.

    Returns:
        Selected turnover profile.
    """
    if turnover_profile is not None:
        return turnover_profile

    possible_profiles = CARE_HOME_TYPE_PROFILES[selected_care_home_type][
        "turnover_profiles"
    ]

    return random_generator.choice(possible_profiles)


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
    care_home_type: str | None = None,
    turnover_profile: str | None = None,
    id_prefix: str = "HOME",
    id_width: int = 4,
    seed: int | None = None,
) -> pd.DataFrame:
    """
    Generate synthetic care home records.

    Args:
        number_of_homes: Number of care homes to generate.
        care_home_type: Optional care home type to apply to all generated homes.
            If None, care home types are randomly selected.
        turnover_profile: Optional turnover profile to apply to all generated homes.
            If None, turnover profiles are selected based on care home type.
        id_prefix: Prefix used for generated care home IDs.
        id_width: Number of digits used in generated care home IDs.
        seed: Optional random seed for reproducible output.

    Returns:
        A pandas DataFrame containing synthetic care home records.

    Raises:
        ValueError: If number_of_homes is less than 1, care_home_type is invalid,
            or turnover_profile is invalid.
    """
    if number_of_homes < 1:
        raise ValueError("number_of_homes must be greater than or equal to 1")

    validate_care_home_type(care_home_type)
    validate_turnover_profile(turnover_profile)

    fake = Faker("en_GB")
    Faker.seed(seed)
    random_generator = Random(seed)

    care_home_ids = generate_ids(id_prefix, number_of_homes, width=id_width)
    records = []
    used_names = set()

    for care_home_id in care_home_ids:
        selected_care_home_type = select_care_home_type(
            random_generator,
            care_home_type,
        )
        selected_turnover_profile = select_turnover_profile(
            selected_care_home_type,
            random_generator,
            turnover_profile,
        )

        occupancy_min, occupancy_max = CARE_HOME_TYPE_PROFILES[
            selected_care_home_type
        ]["occupancy_range"]

        region = random_generator.choice(list(UK_REGIONS_AND_LOCAL_AUTHORITIES.keys()))
        local_authority = random_generator.choice(UK_REGIONS_AND_LOCAL_AUTHORITIES[region])
        bed_capacity = random_generator.randint(20, 90)
        occupancy_rate = round(
            random_generator.uniform(occupancy_min, occupancy_max),
            2,
        )
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
                "care_home_type": selected_care_home_type,
                "turnover_profile": selected_turnover_profile,
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