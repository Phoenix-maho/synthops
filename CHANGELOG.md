# Changelog

All notable changes to SynthOps will be documented in this file.

This project follows the spirit of [Keep a Changelog](https://keepachangelog.com/) and aims to make changes understandable for users, contributors and maintainers.

SynthOps is currently in early development. Version `0.1.0` is the first pre-release and is not a stable `1.0` release.

---

## [Unreleased]

### Added

### Changed

### Fixed

### Documentation

---

## [0.1.0] - 2026-08-25

### Added

- Initial Python package structure using a `src/` layout.
- Core reusable ID generation utilities.
- Core reusable date utilities.
- Adult Social Care domain module structure.
- Scenario-driven `care_homes` generator.
- Adult Social Care `residents` lifecycle generator.
- Time-aware resident generation using `dataset_start_date` and `dataset_end_date`.
- Active, discharged and deceased resident lifecycle records.
- Resident records linked to generated care homes.
- Configurable care home ID prefixes and ID widths.
- Configurable care home type selection.
- Configurable turnover profile selection.
- Care home type-specific occupancy behaviour.
- Synthetic sample `care_homes.csv` output.
- Synthetic sample `residents.csv` output.
- Example script for generating Adult Social Care sample data.
- Automated tests using `pytest`.
- GitHub Actions workflow for automated test runs.
- Initial project README.
- Architecture documentation.
- Project roadmap.
- Contributing guidelines.
- Security policy.
- Code of conduct.
- Architecture decision records.
- Adult Social Care domain documentation.
- Adult Social Care data dictionary.
- High-level architecture diagram.
- Adult Social Care data flow diagram.
- Adult Social Care table relationship diagram.
- GitHub labels, milestones and project board.

### Changed

- Renamed the project direction from a care-only synthetic data generator to a broader synthetic operational data framework.
- Reframed Adult Social Care as the first domain module rather than the entire product.
- Updated care home generation from purely random generation to scenario-driven generation.
- Updated ID generation to support reusable custom ID formats across future domains and tables.
- Updated the Adult Social Care sample generation script to output both care homes and residents.

### Fixed

- Corrected local Git repository boundary so SynthOps is tracked as its own repository.
- Fixed local package import issue by adding `pyproject.toml` and installing the package in editable mode.
- Updated occupancy tests to reflect care home type-specific occupancy ranges.
- Resolved CSV overwrite issue caused by the sample file being open in Excel.
- Removed empty duplicate documentation files to avoid confusion.
- Added missing `CONTRIBUTING.md` file to the repository.

### Documentation

- Added responsible-use language to clarify that SynthOps generates fictional data for learning, analytics development and prototyping.
- Added architecture guidance explaining the separation between core utilities and domain modules.
- Added roadmap phases covering repository foundation, generator implementation, open-source product management and engineering maturity.
- Added design decision records for modular domain architecture and time-aware resident lifecycle modelling.
- Updated Adult Social Care documentation to describe the implemented resident lifecycle generator.
- Added Adult Social Care data dictionary documenting implemented tables, columns, relationships, valid values and data quality rules.
- Added high-level architecture, Adult Social Care data flow and Adult Social Care table relationship diagrams.
- Added contributor guidance covering setup, branching, testing, pull requests and responsible synthetic data contribution.

---

## Release Notes Format

Future releases should group changes under:

- `Added`
- `Changed`
- `Deprecated`
- `Removed`
- `Fixed`
- `Security`
- `Documentation`

Each release should explain changes in plain language so that users, contributors and technical reviewers can understand what changed and why.