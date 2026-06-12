# 📦 Jarjarbin06 — Documentation Standard

> Internal documentation standard used across all Jarjarbin06 projects (libraries, tools, APIs, Makefiles, and frameworks).

---

## 🔹 1. Global Philosophy

The Jarjarbin06 documentation style is built around **clarity, structure, determinism, and technical precision**.

It is designed to:

* Be immediately readable by developers
* Scale from small tools to large frameworks
* Serve both as **user documentation** and **technical reference**
* Be consistent across all repositories and technologies

Core principles:

* **Structured over narrative**
* **Technical over marketing**
* **Explicit over implicit**
* **Deterministic over descriptive ambiguity**
* **Modular and reusable sections**

---

## 🔹 2. Visual Identity

### Header Style

Every README begins with:

```md
# 📦 <Project Name>

> <One-line technical tagline>
```

Rules:

* Emoji (`📦`) is mandatory for identity consistency
* Tagline must be:

  * One sentence
  * Technical (not marketing)
  * Precise and descriptive

---

## 🔹 3. Section System (Canonical Order)

Sections must follow a **strict hierarchical structure**.

---

### 🔹 Short Description

**Purpose:** Immediate understanding of the project.

Format:

```md
## 🔹 Short Description

**<Project> is a <type> that <does what> using <how>.**
```

Rules:

* Always bold first sentence
* Must define:

  * what it is
  * what it does
  * how it works (briefly)

---

### 🔹 Authors

Always present, minimal:

```md
## 🔹 Authors

* Name (alias)
* Organization (optional)
```

---

### 🔹 License

Always explicit:

```md
## 🔹 License

GPL v3
```

(No explanations)

---

### 🔹 Target Audience

Bullet list of **real users**, not vague roles.

Good:

* “C developers working with low-level file handling”

Bad:

* “Anyone who wants to code”

---

### 🔹 Platform Support

Always explicit environment constraints:

* OS compatibility
* Language/runtime
* Dependencies (or absence of)

---

### 🔹 Purpose

This is one of the **most important sections**.

Structure:

```md
## 🔹 Purpose

<Project> aims to:

* Feature 1
* Feature 2
* Feature 3

It is **not <common misconception>**, but a **<precise classification>**.
```

Rules:

* Must include a **negative clarification**
* Must distinguish from similar tools

---

### 🔹 Key Features

Flat bullet list:

* No explanations
* No nesting
* Technical phrasing only

---

## 🔹 4. Architecture Section (Signature Element)

### REQUIRED for most projects

Format:

```
ASCII diagram (boxes + arrows)
```

Rules:

* Top-down flow
* Always linear or branching logic
* No decorative ASCII — only structural
* Must reflect real system design

Purpose:

* Provide immediate mental model

---

## 🔹 5. Core Concept Section

Explains **how the system fundamentally works**.

Includes:

* Data model
* Execution flow
* Contracts (if any)

Often includes:

* Function signatures
* Lifecycle description
* Conceptual breakdown

---

## 🔹 6. API / Function Documentation

### Structured tables or grouped sections

Rules:

* Group by responsibility:

  * Creation
  * Execution
  * Access
  * Destruction
* Always include:

  * Function name
  * Description
* Prefer tables for clarity

---

## 🔹 7. Project Structure

Tree format:

```
project/
├── file
├── folder/
└── ...
```

Rules:

* Must reflect real repo
* No fake files
* Clear naming

---

## 🔹 8. Usage Section

### Must include:

* Minimal example
* Realistic scenario

Rules:

* Code must be executable or close to
* No pseudo-code unless necessary

---

## 🔹 9. Build / Installation

Separate clearly:

### Installation

* pip / make / manual

### Build

* compilation commands

Rules:

* Commands must be copy-paste ready

---

## 🔹 10. Execution Behavior (if applicable)

Used for:

* CLI tools
* engines
* pipelines

Describes:

* runtime flow
* outputs
* processing model

---

## 🔹 11. Memory Model (Advanced Signature)

Frequently present in Jarjarbin06 style.

Describes:

* allocation strategy
* ownership rules
* lifecycle

Rules:

* Low-level, explicit
* Especially for C / systems projects

---

## 🔹 12. Design Philosophy

Short bullet list:

* architectural decisions
* constraints
* priorities

Example:

* deterministic execution
* no hidden state
* modular design

---

## 🔹 13. Current State

Always present.

Structure:

```md
⚠️ <status sentence>

Status:

* implemented features

Limitations:

* missing features
```

Rules:

* Must be honest
* No marketing language

---

## 🔹 14. Limitations

Explicit constraints:

* performance
* missing features
* design tradeoffs

---

## 🔹 15. Extension / Contribution (Optional)

Used when:

* system is modular
* extensibility exists

Includes:

* how to add modules / rules / features
* constraints

---

## 🔹 16. Notes

Free-form but still technical:

* design intent
* usage recommendations
* context

---

## 🔹 17. Writing Style Rules

### Tone

* Formal
* Technical
* Neutral
* No storytelling

---

### Vocabulary

Use:

* “deterministic”
* “modular”
* “structured”
* “explicit”
* “lightweight”

Avoid:

* “awesome”
* “powerful” (unless justified)
* marketing adjectives

---

### Formatting

* Use `## 🔹` for all sections
* Use bold for definitions
* Use monospace for:

  * functions
  * commands
  * paths

---

## 🔹 18. Code Style in Docs

### Python

```python
def example():
    pass
```

### C

```c
int function(void);
```

Rules:

* Minimal but realistic
* No placeholders like `foo/bar` unless generic

---

## 🔹 19. Consistency Rules

Every project must:

* Follow same section order
* Use same section names
* Maintain same tone
* Avoid missing core sections

---

## 🔹 20. Identity Summary

Jarjarbin06 documentation style is:

* Structured like a **specification**
* Written like a **technical manual**
* Organized like a **modular system**
* Designed for **developers, not marketing**

---

## 🔹 Final Rule

> If a section does not provide technical value, it should not exist.

---

Jarjarbin06 — Structured. Modular. Deterministic.
