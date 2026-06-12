# 📦 Jarjarbin06 — BADGES Specification

> Defines the official multi-line badge system used to categorize and visually represent repositories inside the Jarjarbin06 ecosystem.

---

## 🔹 1. Core Principle

Each repository SHOULD define a file named:

```
BADGES
```

This file contains **multiple badge lines** describing:

* ecosystem membership
* technical category
* implementation type
* optional metadata grouping

This system extends `STATUS` and `VERSION` by providing **classification metadata for ecosystem indexing and visualization**.

---

## 🔹 2. File Rules

### 🔹 BADGES (optional but recommended)

File name:

```
BADGES
```

### Content format:

* Multiple lines allowed
* Each line = one badge group or category tag
* Each line MUST be a valid Shields.io badge
* No explanations inside file

Example structure:

![badge](https://img.shields.io/badge/<key>-<value>-<color>?style=flat-square)

```md
![badge](https://img.shields.io/badge/<key>-<value>-<color>?style=flat-square)
```

Rules:

* Unlimited number of lines (recommended: 1–6)
* No empty lines inside logical grouping (except separation of groups)
* Must be deterministic and machine-readable

---

## 🔹 3. Official Jarjarbin06 Badge Categories

Each category has a **strict color assignment** to ensure ecosystem consistency.

---

# 🟦 3.1 Language Ecosystem Tags

### 🐍 Python

![python](https://img.shields.io/badge/language-python-3776AB?style=flat-square)

```md
![python](https://img.shields.io/badge/language-python-3776AB?style=flat-square)
```

Definition:
Python-based libraries, tools, engines, or frameworks.

---

### ⚙️ C

![c](https://img.shields.io/badge/language-c-A8B9CC?style=flat-square)

```md
![c](https://img.shields.io/badge/language-c-A8B9CC?style=flat-square)
```

Definition:
C-based libraries, system tools, or low-level components.

---

# 🟩 3.2 Python Ecosystem Categories

### 📚 Python Library

![python-lib](https://img.shields.io/badge/type-python%20library-2ECC71?style=flat-square)

```md
![python-lib](https://img.shields.io/badge/type-python%20library-2ECC71?style=flat-square)
```

### 🧰 Python Tool

![python-tool](https://img.shields.io/badge/type-python%20tool-27AE60?style=flat-square)

```md
![python-tool](https://img.shields.io/badge/type-python%20tool-27AE60?style=flat-square)
```

### 🎮 Game / Engine

![python-game](https://img.shields.io/badge/type-game%2Fengine-1ABC9C?style=flat-square)

```md
![python-game](https://img.shields.io/badge/type-game%2Fengine-1ABC9C?style=flat-square)
```

---

# 🟥 3.3 C Ecosystem Categories

### 📦 C Library

![c-lib](https://img.shields.io/badge/type-c%20library-A8B9CC?style=flat-square)

```md
![c-lib](https://img.shields.io/badge/type-c%20library-A8B9CC?style=flat-square)
```

### 🔧 C System Utility

![c-system](https://img.shields.io/badge/type-system%20utility-5D6D7E?style=flat-square)

```md
![c-system](https://img.shields.io/badge/type-system%20utility-5D6D7E?style=flat-square)
```

### 🧠 C Data Structure / Core Engine

![c-core](https://img.shields.io/badge/type-core%20system-34495E?style=flat-square)

```md
![c-core](https://img.shields.io/badge/type-core%20system-34495E?style=flat-square)
```

---

# 🟨 3.4 Application Type Tags

### 🎮 Game

![game](https://img.shields.io/badge/domain-game-F1C40F?style=flat-square)

```md
![game](https://img.shields.io/badge/domain-game-F1C40F?style=flat-square)
```

### 🧪 Tool / Utility

![tool](https://img.shields.io/badge/domain-tool-F39C12?style=flat-square)

```md
![tool](https://img.shields.io/badge/domain-tool-F39C12?style=flat-square)
```

### 🧩 Framework / Engine

![engine](https://img.shields.io/badge/domain-engine-E67E22?style=flat-square)

```md
![engine](https://img.shields.io/badge/domain-engine-E67E22?style=flat-square)
```

---

# 🟪 3.5 Architecture Tags

### 🔌 Wrapper

![wrapper](https://img.shields.io/badge/architecture-wrapper-9B59B6?style=flat-square)

```md
![wrapper](https://img.shields.io/badge/architecture-wrapper-9B59B6?style=flat-square)
```

### 🧱 Core Library

![core](https://img.shields.io/badge/architecture-core-8E44AD?style=flat-square)

```md
![core](https://img.shields.io/badge/architecture-core-8E44AD?style=flat-square)
```

### 🧪 Experimental Module

![experimental](https://img.shields.io/badge/architecture-experimental-8E44AD?style=flat-square)

```md
![experimental](https://img.shields.io/badge/architecture-experimental-8E44AD?style=flat-square)
```

---

# 🟫 3.6 System Quality Tags

### ⚡ Lightweight

![lightweight](https://img.shields.io/badge/quality-lightweight-16A085?style=flat-square)

```md
![lightweight](https://img.shields.io/badge/quality-lightweight-16A085?style=flat-square)
```

### 🧠 Low-level

![lowlevel](https://img.shields.io/badge/quality-low--level-2C3E50?style=flat-square)

```md
![lowlevel](https://img.shields.io/badge/quality-low--level-2C3E50?style=flat-square)
```

### 🔒 Secure

![secure](https://img.shields.io/badge/quality-secure-2ECC71?style=flat-square)

```md
![secure](https://img.shields.io/badge/quality-secure-2ECC71?style=flat-square)
```

---

# 🔷 4. Ecosystem Rules for BADGES File

## 🔹 4.1 Structure Rules

A repository BADGES file SHOULD follow ordering:

1. Language
2. Type
3. Domain
4. Architecture
5. Quality

Example:

```
(language)
(type)
(domain)
(architecture)
(quality)
```

---

## 🔹 4.2 Example BADGES File (C Library)

![language](https://img.shields.io/badge/language-c-A8B9CC?style=flat-square)
![type](https://img.shields.io/badge/type-c%20library-A8B9CC?style=flat-square)
![domain](https://img.shields.io/badge/domain-tool-F39C12?style=flat-square)
![architecture](https://img.shields.io/badge/architecture-core-8E44AD?style=flat-square)
![quality](https://img.shields.io/badge/quality-low--level-2C3E50?style=flat-square)

---

## 🔹 4.3 Example BADGES File (Python Game Engine)

![language](https://img.shields.io/badge/language-python-3776AB?style=flat-square)
![type](https://img.shields.io/badge/type-game%2Fengine-1ABC9C?style=flat-square)
![domain](https://img.shields.io/badge/domain-engine-E67E22?style=flat-square)
![architecture](https://img.shields.io/badge/architecture-core-8E44AD?style=flat-square)
![quality](https://img.shields.io/badge/quality-lightweight-16A085?style=flat-square)

---

## 🔹 5. Mapping Your Ecosystem

### 🐍 Python projects (your list)

* default language: `python`
* type:

  * toolkit → `python library`
  * console/tools → `python tool`
  * game/engine → `game/engine`

---

### ⚙️ C projects

* default language: `c`
* type:

  * lib* → `c library`
  * system helpers → `system utility`
  * core structures → `core system`

---

## 🔹 6. BADGES vs STATUS Separation Rule

* `STATUS` → lifecycle (single truth)
* `VERSION` → release identity
* `BADGES` → classification metadata

These MUST NEVER overlap in meaning:

| File    | Purpose                   |
| ------- | ------------------------- |
| STATUS  | lifecycle state           |
| VERSION | semantic version          |
| BADGES  | structural classification |

---

## 🔹 7. Final Constraint

> BADGES MUST describe what the project IS, not how stable it is.

---
