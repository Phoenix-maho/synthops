# Security Policy

## Overview

SynthOps is an open-source synthetic operational data generation framework.

The project is designed to generate fictional datasets for analytics engineering, business intelligence, AI prototyping and decision-intelligence use cases.

Although SynthOps does not use real personal, clinical, financial, employment or organisational records, security and responsible data handling are still important because the project may be used in sensitive operational domains such as adult social care, finance, construction, workforce analytics and public services.

---

## Supported Versions

SynthOps is currently in early development and has not yet published a stable release.

| Version | Supported |
|---|---|
| `main` branch | Yes, best-effort support |
| Pre-release versions | Yes, best-effort support |
| Stable releases | Not available yet |

Security guidance will become more formal as the project approaches stable releases.

---

## What Counts as a Security or Safety Issue?

Please report an issue if you identify any of the following:

- generated data that appears to contain real personal information
- generated data that could be mistaken for a real person, care provider, organisation or financial record
- accidental inclusion of real data in sample files
- unsafe assumptions that could encourage misuse of generated data
- code that exposes local files, credentials, secrets or environment variables
- dependency vulnerabilities
- unsafe file-writing behaviour
- insecure example usage
- misleading documentation about the purpose or limitations of generated data

---

## Sensitive Data Policy

SynthOps must not contain real sensitive data.

Contributors must not add:

- real resident, patient, staff or provider records
- real names linked to care records
- real addresses linked to individuals
- real NHS numbers or health identifiers
- real national insurance numbers
- real phone numbers or email addresses belonging to individuals
- real financial account details
- real employment records
- real safeguarding records
- real clinical records
- real commercially confidential datasets

All sample data must be fictional.

---

## Responsible Synthetic Data Use

Generated data from SynthOps is intended for:

- learning
- analytics engineering practice
- dashboard development
- data modelling
- AI prototyping
- software testing
- decision-intelligence demonstrations

Generated data must not be used for:

- clinical decision-making
- safeguarding decisions
- regulatory reporting
- financial decisions
- employment decisions
- inspection judgements
- real-world evaluation of individuals, providers, organisations or services

Synthetic data should not be presented as real data.

Synthetic modelling assumptions should not be presented as official statistics or real-world benchmarks.

---

## Reporting a Security Issue

If you find a security or responsible-data issue, please do not open a public GitHub issue if the report includes sensitive details.

Instead, use one of the following routes:

1. Open a private security advisory on GitHub, if available.
2. Contact the maintainer directly through the contact method listed on the maintainer's GitHub profile.
3. If the issue does not contain sensitive details, open a GitHub issue and clearly label it as a security, safety or responsible-data concern.

When reporting, please include:

- a clear description of the issue
- steps to reproduce the issue, if relevant
- affected files or functions
- why the issue may create risk
- any suggested fix, if available

---

## Example Responsible-Data Issues

Examples of issues that should be reported include:

- a generated care home name matching a real provider in a way that could cause confusion
- a sample CSV accidentally containing real data
- generated resident data including full name, full date of birth and address together
- documentation implying the generated data can be used for real care-quality assessment
- a generator producing unrealistic or misleading risk patterns without explanation
- sample outputs being too similar to a real organisation's operational data

---

## Secrets and Credentials

SynthOps should not require secrets or credentials for local generation.

Do not commit:

- API keys
- passwords
- tokens
- connection strings
- private configuration files
- cloud credentials
- service-account files

If secrets are accidentally committed, remove them from the repository and rotate them immediately.

---

## Dependencies

SynthOps currently uses a small Python dependency set.

Current key dependencies include:

- `pandas`
- `numpy`
- `faker`
- `pytest`

Dependency security checks may be added in a later development phase using GitHub Actions or dependency scanning.

---

## Maintainer Response

For valid security or responsible-data reports, the maintainer will aim to:

1. acknowledge the report
2. assess the risk
3. reproduce the issue where possible
4. decide whether a code, data or documentation change is needed
5. prioritise fixes based on severity
6. document the fix in the changelog where appropriate

Response times may vary while the project is in early development.

---

## Disclosure Policy

Please avoid publicly disclosing sensitive details before the maintainer has had reasonable time to assess and address the issue.

For non-sensitive documentation or modelling concerns, public GitHub issues are welcome.

---

## Security Roadmap

Future security and responsible-data improvements may include:

- GitHub security advisories
- dependency scanning
- automated test workflow
- generated data validation checks
- responsible-use checklist for new domains
- contribution review checklist
- clearer release security notes
- guidance for safe synthetic data publication

---

## Summary

SynthOps is designed to generate fictional operational datasets safely and responsibly.

Security in this project includes both traditional software security and responsible synthetic data practice. The project should remain free from real sensitive data, clear about its limitations and careful about how generated data may be interpreted or reused.