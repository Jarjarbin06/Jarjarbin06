# 📦 Jarjarbin06 — Repository Status & Versioning Standard

> Defines the official lifecycle state system and versioning mechanism used across all Jarjarbin06 repositories.

---

## 🔹 1. Core Principle

Each repository SHOULD explicitly declare:

* its **lifecycle state** (development status)
* its **current version**

These are stored as **dedicated root files**, not embedded in README.

This ensures:

* deterministic parsing
* tooling compatibility
* consistent ecosystem indexing

---

## 🔹 2. Required Files

### 🔹 STATUS (mandatory)

A file named exactly:

```
STATUS
```

### Content:

A single badge line only (no extra text):

```md
![status](https://img.shields.io/badge/status-<state>-<color>?style=flat-square)
```

Rules:

* Only ONE badge allowed
* Must match one of the official Jarjarbin06 statuses
* No comments, no metadata, no formatting
* Must be machine-readable

---

### 🔹 VERSION (mandatory)

A file named exactly:

```
VERSION
```

### Content:

Single semantic version string:

```
vX.Y.Z
```

Examples:

```
v1.0.0
v0.2.3
v3.14.1
```

Rules:

* Must start with `v`
* Must follow semantic versioning
* No additional text allowed
* One line only

---

## 🔹 3. Official Jarjarbin06 Status Badges

These are the **ONLY valid lifecycle states**.

---

### 🔴 deprecated

```md
![status](https://img.shields.io/badge/status-deprecated-red?style=flat-square)
```

**Definition:**
No longer maintained. Superseded by a newer implementation. Usage is discouraged and may cause incompatibilities.

---

### 🟢 stable

```md
![status](https://img.shields.io/badge/status-stable-brightgreen?style=flat-square)
```

**Definition:**
Production-ready state with stable API guarantees and no expected breaking changes.

---

### 🟡 development

```md
![status](https://img.shields.io/badge/status-development-yellow?style=flat-square)
```

**Definition:**
Actively developed. Features are incomplete or evolving. API may change without notice.

---

### 🟣 experimental

```md
![status](https://img.shields.io/badge/status-experimental-purple?style=flat-square)
```

**Definition:**
Prototype-level implementation. Used for validation of concepts. Not stable or production-safe.

---

### 🔵 maintained

```md
![status](https://img.shields.io/badge/status-maintained-blue?style=flat-square)
```

**Definition:**
Actively maintained with updates and fixes, but without strict API stability guarantees.

---

### ⚫ archived

```md
![status](https://img.shields.io/badge/status-archived-lightgrey?style=flat-square)
```

**Definition:**
Frozen repository state. No further development. Kept for reference or historical purposes.

---

### 🟠 testing

```md
![status](https://img.shields.io/badge/status-testing-orange?style=flat-square)
```

**Definition:**
Used exclusively for validation, QA, or internal verification workflows. Not production intended.

---

### 🟠 WIP

```md
![status](https://img.shields.io/badge/status-WIP-orange?style=flat-square)
```

**Definition:**
Work in progress. Implementation incomplete and may be non-functional.

---

### 🔵 frozen

```md
![status](https://img.shields.io/badge/status-frozen-blue?style=flat-square)
```

**Definition:**
Finalized state. No modifications allowed, even if functional. Used for locked core versions.

---

## 🔹 4. State Selection Rules

Each repository MUST define exactly one status.

Rules:

* `experimental` → early prototype
* `development` → active build phase
* `WIP` → incomplete but actively edited
* `testing` → validation phase only
* `maintained` → stable maintenance without API guarantee
* `stable` → production-ready and version-locked API
* `frozen` → immutable state
* `deprecated` → replaced and discouraged
* `archived` → no further activity

---

## 🔹 5. Versioning Rules

Versioning MUST follow semantic structure:

```
vMAJOR.MINOR.PATCH
```

Rules:

* MAJOR → breaking changes
* MINOR → feature additions (backward compatible)
* PATCH → fixes only

Additional constraints:

* Version must always exist if STATUS exists
* Version must be manually updated (no implicit inference)

---

## 🔹 6. System Behavior Summary

Each repository is defined by:

```
/STATUS   → lifecycle state (single badge)
/VERSION  → semantic version string
README    → documentation (optional but recommended)
```

This forms a **minimal deterministic metadata layer** for tooling, indexing, and ecosystem tracking.

---

## 🔹 7. Identity Constraint

Jarjarbin06 repositories are:

* explicitly state-driven
* externally readable without parsing README
* structured for automation and tooling integration
* strictly constrained in lifecycle definition

---
