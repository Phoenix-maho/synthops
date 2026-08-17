# Changelog

All notable changes to SynthOps will be documented in this file.

This project follows the spirit of [Keep a Changelog](https://keepachangelog.com/) and aims to make changes understandable for users, contributors and maintainers.

SynthOps is currently in early development and has not yet published a stable release.

---

## [Unreleased]

### Added

- Initial Python package structure using a `src/` layout.
- Core reusable ID generation utilities.
- Core reusable date utilities.
- Adult Social Care domain module structure.
- Scenario-driven `care_homes` generator.
- Configurable care home ID prefixes and ID widths.
- Configurable care home type selection.
- Configurable turnover profile selection.
- Care home type-specific occupancy behaviour.
- Synthetic sample `care_homes.csv` output.
- Example script for generating Adult Social Care sample data.
- Automated tests using `pytest`.
- Initial project README.
- Architecture documentation.
- Project roadmap.

### Changed

- Renamed the project direction from a care-only synthetic data generator to a broader synthetic operational data framework.
- Reframed Adult Social Care as the first domain module rather than the entire product.
- Updated care home generation from purely random generation to scenario-driven generation.
- Updated ID generation to support reusable custom ID formats across future domains and tables.

### Fixed

- Corrected local Git repository boundary so SynthOps is tracked as its own repository.
- Fixed local package import issue by adding `pyproject.toml` and installing the package in editable mode.
- Updated occupancy tests to reflect care home type-specific occupancy ranges.
- Resolved CSV overwrite issue caused by the sample file being open in Excel.

### Documentation

- Added responsible-use language to clarify that SynthOps generates fictional data for learning, analytics development and prototyping.
- Added architecture guidance explaining the separation between core utilities and domain modules.
- Added roadmap phases covering repository foundation, generator implementation, open-source product management and engineering maturity.

---

## [0.1.0] - Planned

### Planned scope

The first pre-release will focus on establishing SynthOps as a credible open-source project foundation.

Expected scope:

- Repository documentation foundation.
- Adult Social Care `care_homes` generator.
- Core ID and date utilities.
- Sample CSV output.
- Test coverage for current generator behaviour.
- Initial GitHub issues and milestones.
- Clear responsible-use guidance.

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