# HLD Model

The HLD (High-Level Design) model defines the architectural intent of the platform.

The HLD describes:

* What the platform should be
* Platform topology
* High availability strategy
* Multi-AZ / Multi-region requirements
* Networking architecture
* Storage architecture
* Security segmentation
* Identity and governance requirements
* Resiliency objectives
* Non-functional requirements

The HLD is:

* Declarative
* Technology-aware but implementation-agnostic
* Cloud-aligned
* Governance-oriented

The HLD does not contain:

* Platform-specific configurations
* IP-level implementation details
* Service configuration files
* Runtime tuning parameters

---

# Purpose

The HLD acts as:

> Source of truth for architecture.

It provides the architectural foundation used to:

* Validate platform consistency
* Generate LLD artifacts
* Apply governance controls
* Validate compliance requirements
* Drive deployment orchestration

---

# Example

```yaml
platform:
  type: private-cloud

high_availability: true

availability_zones:
  - az1
  - az2
  - az3

networking:
  segmentation: strict
  overlay: geneve

storage:
  distributed: true
  replication: 3

identity:
  federation: true
  zero_trust: true
```

---

# Relationship with the LLD

The HLD defines:

> What the platform should be.

The LLD defines:

> How the platform is implemented.
