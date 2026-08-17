from synthops.domains.adult_social_care.care_homes import generate_care_homes
from synthops.domains.adult_social_care.residents import generate_residents


def main() -> None:
    care_homes = generate_care_homes(
        number_of_homes=10,
        id_prefix="HM",
        id_width=3,
        seed=42,
    )

    residents = generate_residents(
        care_homes=care_homes,
        dataset_start_date="2020-01-01",
        dataset_end_date="2024-12-31",
        id_prefix="RES",
        id_width=5,
        seed=42,
    )

    print("\nGenerated care homes:")
    print(care_homes)

    print("\nGenerated residents:")
    print(residents.head())

    care_homes_output_path = "data/sample/adult_social_care/care_homes.csv"
    residents_output_path = "data/sample/adult_social_care/residents.csv"

    care_homes.to_csv(care_homes_output_path, index=False)
    residents.to_csv(residents_output_path, index=False)

    print(f"\nSaved care homes sample data to: {care_homes_output_path}")
    print(f"Saved residents sample data to: {residents_output_path}")


if __name__ == "__main__":
    main()