# 📊 CICD-TextStats
CI/CD-ready Python CLI that computes text statistics and showcases engineering best practices.

Tiny Python CLI that analyzes text **and** demonstrates **CI/CD best practices**.
It serves two purposes:
1. **Practical tool** → Analyze text quickly from the command line.
2. **Showcase project** → Clean repo structure, tests, and GitHub Actions CI/CD.

[![CI](https://img.shields.io/github/actions/workflow/status/airdmhund1/cicd-textstats/ci.yml?branch=main)](https://github.com/airdmhund1/cicd-textstats/actions)
![coverage](assets/coverage.svg)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](#)

## ✨ Features
- Simple CLI to compute:
  - Number of **characters, words, lines**
  - **Top-N most frequent words**
- **Clean Python packaging** (`src/` layout + console entry point)
- **Engineering best practices**:
  - Linting (ruff)
  - Type-checking (mypy)
  - Unit tests (pytest + coverage ≥90%)
  - Pre-commit hooks
- **CI/CD** with GitHub Actions (multi-Python matrix, cached installs)
- **Coverage badge** auto-generated from `coverage.xml`

---
## 🚀 Quickstart

Clone and install:
```bash
git clone https://github.com/airdmhund1/CICD-TextStats.git
cd CICD-TextStats

# setup venv
python -m venv .venv && source .venv/bin/activate

# install dev tools
make install
```

Run CLI:
```bash
# Inline text
textstat-mini --text "Hello hello world" --top 2

# From file
textstat-mini --file examples/sample.txt

# From stdin
echo "stream input goes here" | textstat-mini
```

Example output:
```
# Text Stats
chars: 23
words: 3
lines: 1

# Top Words
hello: 2
world: 1
```

---

## 🧪 Development

Quality checks:
```bash
make lint     # ruff lint
make type     # mypy type-check
make test     # pytest
make cov      # pytest + coverage.xml + badge
```

Run all in one go:
```bash
make all
```
---

## 📂 Project Structure
```
textstat-mini/
├─ .github/workflows/ci.yml     # CI pipeline
├─ assets/coverage.svg          # coverage badge (generated)
├─ examples/sample.txt           # demo file
├─ scripts/gen_coverage_badge.py # local badge generator
├─ src/textstat_mini/            # package code
│  ├─ __init__.py
│  ├─ core.py
│  └─ cli.py
├─ tests/                        # unit tests
├─ pyproject.toml
├─ requirements-dev.txt
├─ Makefile
└─ README.md
```

---

## 🎯 Why this project?
This repo is intentionally **small but polished**:

🔹 **As a CLI tool**
- Lets you analyze text quickly from terminal
- Handles inline text, files, or stdin
- Shows top word frequencies in seconds

🔹 **As a CI/CD showcase**
- Demonstrates modern Python repo standards
- Tests + coverage enforced with a 90% threshold
- Automated lint, type-check, and pre-commit hooks
- GitHub Actions workflow runs across Python versions
