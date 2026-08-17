# 0001: Modular Domain Architecture

## Status

Accepted

## Date

2026-08-17

## Context

SynthOps is being developed as an open-source synthetic operational data generation framework.

The first implemented domain is Adult Social Care, starting with synthetic care home data. However, the long-term goal of SynthOps is broader than care data. The project should eventually support additional operational domains such as finance operations, construction operations, SaaS metrics and workforce analytics.

This creates an architectural decision:

Should SynthOps be built as a care-specific data generator, or should it be built as a domain-agnostic framework with separate domain modules?

The decision matters because early structure can either support or block future extensibility.

If all logic is placed directly into one care-focused module, the project may become difficult to extend later. Future domains could require duplicated ID logic, duplicated date utilities, inconsistent generation patterns and unclear boundaries between reusable engine code and domain-specific assumptions.

SynthOps is intended to be a professional open-source product, not a one-off script. The architecture should support maintainability, testing, documentation, contributor onboarding and future domain expansion.

## Decision

SynthOps will use a modular domain architecture.

Reusable logic will live in the core package:

```text
src/synthops/core/
```

Domain-specific logic will live in separate domain modules:

```text
src/synthops/domains/
```

The current first domain module is:

```text
src/synthops/domains/adult_social_care/
```

Future domain modules may include:

```text
src/synthops/domains/finance_operations/
src/synthops/domains/construction_operations/
src/synthops/domains/saas_metrics/
src/synthops/domains/workforce_analytics/
```

The core package should contain reusable utilities such as:

- ID generation
- date utilities
- validation helpers
- export helpers
- shared configuration patterns

Domain modules should contain:

- domain entities and tables
- domain-specific assumptions
- scenario drivers
- value ranges
- relationship rules
- domain documentation
- domain-specific examples and tests

Adult Social Care will be treated as the first domain module, not as the entire product.

## Alternatives Considered

### Alternative 1: Build SynthOps as a care-only generator

This would have been simpler at the beginning.

Possible advantages:

- faster initial development
- fewer folders and abstractions
- easier for a beginner to understand at first
- less upfront architecture work

Disadvantages:

- harder to expand beyond Adult Social Care
- reusable logic may become mixed with care-specific assumptions
- future domains may require duplicated code
- the project may look like a narrow portfolio exercise
- contributor onboarding may become harder as the project grows

This option was rejected because it does not support the long-term product vision.

### Alternative 2: Build a highly abstract generation engine immediately

This would involve designing a more advanced generic engine before building much domain functionality.

Possible advantages:

- strong theoretical extensibility
- consistent structure across all future domains
- easier to enforce common generation patterns later

Disadvantages:

- risk of over-engineering too early
- slower progress on useful generated datasets
- abstractions may be wrong before enough domain examples exist
- harder for new contributors to understand
- could make the project feel unnecessarily complex

This option was rejected for now because SynthOps is still early and needs practical domain implementation before heavy abstraction.

### Alternative 3: Use a modular structure with light shared core utilities

This approach separates reusable core utilities from domain-specific modules without over-engineering the framework too early.

Advantages:

- keeps Adult Social Care implementation practical
- preserves a clear path to future domains
- avoids premature abstraction
- supports testing and documentation by module
- makes repository structure easier to explain
- improves maintainability and contributor onboarding

Disadvantages:

- requires more initial structure than a single script
- some patterns may need refactoring as more domains are added
- the boundary between core and domain code must be reviewed regularly

This option was accepted.

## Consequences

### Positive Consequences

This decision supports:

- clearer separation of concerns
- reusable utilities across domains
- better test organisation
- easier future domain expansion
- stronger documentation structure
- more professional repository presentation
- better contributor onboarding
- stronger alignment with open-source product expectations

It also supports the positioning of SynthOps as a synthetic operational data framework rather than a narrow synthetic care dataset generator.

### Negative Consequences

This decision introduces slightly more complexity at the start.

New contributors need to understand the difference between:

```text
core logic
```

and:

```text
domain-specific logic
```

There is also a risk that some utilities may be placed in the wrong layer early on. For example, a function that appears reusable may later turn out to be domain-specific, or a domain-specific pattern may later deserve promotion into the core package.

This will be handled through review and refactoring as the project matures.

## Implementation Notes

The current structure follows this decision:

```text
src/synthops/
├── core/
│   ├── ids.py
│   └── dates.py
│
└── domains/
    └── adult_social_care/
        └── care_homes.py
```

Current reusable utilities:

- `generate_id`
- `generate_ids`
- `parse_date`
- `generate_date_range`
- `random_date_between`

Current Adult Social Care generator:

- `generate_care_homes`

The `care_homes` generator uses core utilities for reusable behaviours such as ID generation while keeping care-specific assumptions inside the Adult Social Care domain module.

## Design Rules Going Forward

When adding new functionality, use the following rules.

### Put logic in `core` when it is:

- reusable across multiple domains
- not dependent on Adult Social Care terminology
- useful for ID generation, dates, validation, export or shared configuration
- likely to be needed by finance, construction, SaaS or workforce modules later

### Put logic in a domain module when it is:

- specific to a sector or operational domain
- based on domain-specific assumptions
- tied to domain entities such as residents, care homes, invoices or projects
- using domain-specific value ranges or scenario rules
- unlikely to be reusable without modification

## Review Trigger

This decision should be reviewed when:

- a second domain module is introduced
- shared validation logic becomes duplicated
- export behaviour becomes common across domains
- configuration patterns become repeated
- the project introduces a command-line interface
- the project approaches a stable release

At that point, some logic may need to move from domain modules into the core package.

## Summary

SynthOps will use a modular domain architecture.

The project will keep reusable generation utilities in `src/synthops/core/` and domain-specific logic in `src/synthops/domains/`.

This decision supports the long-term goal of building a professional, maintainable and extensible open-source synthetic operational data framework.