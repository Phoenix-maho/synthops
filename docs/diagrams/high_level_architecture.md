# High-Level Architecture Diagram

This diagram shows the current high-level architecture of SynthOps.

SynthOps separates reusable core utilities from domain-specific generation logic. Adult Social Care is the first implemented domain module, while future domains can reuse the same core utilities.

```mermaid
flowchart TD
    A[SynthOps] --> B[Core Utilities]
    A --> C[Domain Modules]
    A --> D[Examples]
    A --> E[Tests]
    A --> F[Documentation]

    B --> B1[ID Generation]
    B --> B2[Date Utilities]
    B --> B3[Future Validation Helpers]
    B --> B4[Future Export Helpers]

    C --> C1[Adult Social Care]
    C --> C2[Future Finance Operations]
    C --> C3[Future Construction Operations]
    C --> C4[Future SaaS Metrics]
    C --> C5[Future Workforce Analytics]

    C1 --> C1A[Care Homes Generator]
    C1 --> C1B[Residents Generator]
    C1 --> C1C[Planned Care Needs History]
    C1 --> C1D[Planned Staff, Shifts and Incidents]

    D --> D1[Generate Adult Social Care Sample]
    E --> E1[Pytest Test Suite]
    F --> F1[README]
    F --> F2[Architecture]
    F --> F3[Roadmap]
    F --> F4[Domain Docs]
    F --> F5[ADRs]
    F --> F6[Data Dictionary]
```

## Notes

The core package should remain domain-neutral.

Domain-specific logic should live inside `src/synthops/domains/`.

Adult Social Care is the first implemented domain, not the entire product.