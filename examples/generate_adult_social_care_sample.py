"""
Example script for generating a small Adult Social Care sample dataset.

This script demonstrates how to use SynthOps to generate synthetic care home data.
"""

from synthops.domains.adult_social_care.care_homes import generate_care_homes


def main() -> None:
    care_homes = generate_care_homes(
    number_of_homes=10,
    id_prefix="HM",
    id_width=3,
    seed=42,
)

    print("\nGenerated care homes:")
    print(care_homes)

    output_path = "data/sample/adult_social_care/care_homes.csv"
    care_homes.to_csv(output_path, index=False)

    print(f"\nSaved sample data to: {output_path}")


if __name__ == "__main__":
    main()