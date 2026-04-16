# 📊 Datakit — Lightweight Dataset Profiler

A fast, CLI-first dataset profiling tool for quickly understanding CSV files.

Datakit provides instant insights into your data including:

* column types
* missing values
* uniqueness
* basic distribution signals

---

# 🚀 Features

* 📁 CSV dataset loading
* 📊 Automatic column profiling
* 🧠 Type detection (numeric, categorical, etc.)
* ❌ Missing value detection
* 🔍 Uniqueness analysis
* ⚡ Lightweight CLI flag system
* 🔧 Extensible analysis pipeline (correlation + insights coming next)

---

# 📦 Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd datakit
```

Install dependencies:

```bash
pip install pandas
```

---

# ⚡ Usage

## Basic usage

```bash
python main.py --file data.csv
```

---

## Example output

```text
Dataset: data.csv
Rows: 1200
Columns: 8

━━━ Column Overview ━━━

age int64
  - Unique: 45
  - Missing: 2.3%

country object
  - Unique: 5
  - Missing: 0.0%

salary int64
  - Unique: 812
  - Missing: 0.0%
```

---

# 🧠 CLI Flags

Datakit uses a lightweight custom flag system.

## Required

### `--file`

CSV file to analyse

```bash
--file data.csv
```

Validator:

* must contain `.csv`

---

## Optional

### `--top`

Show top N values in numeric columns

```bash
--top 10
```

---

### `--corr-threshold`

Set correlation sensitivity (coming soon)

```bash
--corr-threshold 0.7
```

---

### `--include`

Only analyse selected columns

```bash
--include age,salary
```

---

### `--exclude`

Exclude specific columns

```bash
--exclude user_id
```

---

### `--format-text`

Output format (future feature)

```bash
--format-text pretty
```

---

### `--no-insights`

Disable insight generation (future feature)

```bash
--no-insights
```

---

# 🧱 Architecture

Datakit is split into two core parts:

## 1. CLI Layer

Handles:

* argument parsing
* validation
* runtime configuration

Built using a lightweight custom flag system:

```python
Flags()
.add_file(...)
.add(...)
.parse_and_resolve(...)
```

---

## 2. Analysis Layer

Handles:

* dataset loading (pandas)
* column profiling
* missing value detection
* uniqueness analysis

Future additions:

* correlation engine
* insight generation
* anomaly detection

---

# 📊 Current Capabilities

### Column profiling

* detects data type
* counts unique values
* calculates missing percentage
* shows top values (numeric columns)

---

### Dataset summary

* row count
* column count
* basic structure overview

---

# 🧠 Design Philosophy

Datakit is built around:

* **fast feedback loops** (run → understand instantly)
* **minimal configuration**
* **CLI-first design**
* **extensible analysis pipeline**

The goal is not to replace pandas, but to provide:

> “instant understanding of a dataset without writing analysis code”

---

# 🔮 Roadmap

## v0.2

* correlation engine
* column filtering (--include / --exclude)

## v0.3

* insight generation layer
* better formatting system

## v0.4

* JSON / HTML output modes
* report export

## v1.0

* stable CLI tool
* plugin-ready architecture

---

# ⚠️ Notes

* Works best with clean CSV files
* Large datasets may require optimization in future versions
* Designed for exploratory analysis, not production ETL pipelines

---

# 🧠 Why this project exists

Most data workflows require writing repetitive pandas code just to understand a dataset.

Datakit solves:

> “I just want to know what’s inside this file immediately”