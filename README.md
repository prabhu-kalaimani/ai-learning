# AI Learning — NLP & LLM with Python

A hands-on learning repository for **Natural Language Processing (NLP)** and **Large Language Models (LLM)** concepts using Python.

> **Confluence:** [PK AI Learning Space](https://prabhukalaimani.atlassian.net/wiki/spaces/Learnings/overview?homepageId=950448)  
> **MkDocs Site:** [prabhu-kalaimani.github.io/ai-learning](https://prabhu-kalaimani.github.io/ai-learning/)

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Clone the Repository](#clone-the-repository)
3. [Setup with VS Code](#setup-with-vs-code)
4. [Setup with PyCharm](#setup-with-pycharm)
5. [Running Tests](#running-tests)
6. [Linting & Formatting](#linting--formatting)
7. [Running the Docs Site](#running-the-docs-site)
8. [Project Structure](#project-structure)
9. [Topics Covered](#topics-covered)

---

## Prerequisites

Install the following tools before proceeding:

| Tool | Version | Download |
|------|---------|----------|
| Python | 3.12 – 3.13 | https://www.python.org/downloads/ |
| Poetry | latest | https://python-poetry.org/docs/#installation |
| Git | latest | https://git-scm.com/downloads |

### Verify installations

```bash
python --version        # Python 3.12.x or 3.13.x
poetry --version        # Poetry 2.x.x
git --version
```

### Install Poetry (if not installed)

**Windows (PowerShell):**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

After installation, add Poetry to your PATH if prompted, then restart your terminal.

---

## Clone the Repository

```bash
git clone <your-repo-url>
cd ai-learning
```

---

## Setup with VS Code

### Step 1 — Install VS Code Extensions

Open VS Code and install these extensions (search in the Extensions panel `Ctrl+Shift+X`):

- **Python** (`ms-python.python`) — core Python support
- **Pylance** (`ms-python.vscode-pylance`) — IntelliSense and type checking
- **Ruff** (`charliermarsh.ruff`) — linting and formatting
- **Even Better TOML** (`tamasfe.even-better-toml`) — for editing `pyproject.toml`

### Step 2 — Install dependencies with Poetry

Open the integrated terminal (`Ctrl+`` `) and run:

```bash
poetry install
```

This creates a `.venv` folder inside the project and installs all dependencies defined in `pyproject.toml`.

### Step 3 — Point VS Code to the Poetry virtual environment

1. Press `Ctrl+Shift+P` → type **Python: Select Interpreter**
2. Choose **Enter interpreter path...**
3. Enter the path to the venv Python:
   - **Windows:** `.venv\Scripts\python.exe`
   - **macOS/Linux:** `.venv/bin/python`

Alternatively, run this in the terminal to get the exact path:

```bash
poetry env info --path
```

Then append `\Scripts\python.exe` (Windows) or `/bin/python` (macOS/Linux) to that path.

### Step 4 — Configure VS Code workspace settings

Create or update `.vscode/settings.json` in the project root:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  },
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests/"],
  "python.analysis.extraPaths": ["src"]
}
```

> On macOS/Linux change the interpreter path to `.venv/bin/python`.

### Step 5 — Verify setup

Open any `.py` file — you should see IntelliSense working. Run the test suite from the Testing panel (`Ctrl+Shift+P` → **Testing: Run All Tests**) or from the terminal:

```bash
poetry run pytest tests/
```

---

## Setup with PyCharm

### Step 1 — Open the project

1. Launch PyCharm
2. **File → Open** → select the `ai-learning` folder
3. Click **OK / Trust Project**

### Step 2 — Configure the Poetry interpreter

1. Go to **File → Settings** (`Ctrl+Alt+S`) → **Project: ai-learning → Python Interpreter**
2. Click the gear icon ⚙ → **Add Interpreter → Add Local Interpreter**
3. Select **Poetry Environment** from the left panel
4. Choose **Existing environment** if the `.venv` already exists, or **New environment** to let PyCharm create it
5. Poetry executable path (if not auto-detected):
   - **Windows:** `%APPDATA%\Python\Scripts\poetry.exe`
   - **macOS/Linux:** `$HOME/.local/bin/poetry`
6. Click **OK**

If you don't see the Poetry option, install Poetry first and restart PyCharm.

### Step 3 — Install dependencies

Open the **Terminal** tab at the bottom (or `Alt+F12`) and run:

```bash
poetry install
```

PyCharm will automatically detect new packages after the install completes.

### Step 4 — Mark `src` as Sources Root

The project uses a `src/` layout. Tell PyCharm where the source is:

1. In the **Project** panel on the left, right-click the `src` folder
2. Select **Mark Directory as → Sources Root**

This enables correct import resolution for `ai_learning.*` imports.

### Step 5 — Configure pytest as the test runner

1. **File → Settings → Tools → Python Integrated Tools**
2. Set **Default test runner** to `pytest`
3. Click **OK**

### Step 6 — Configure Ruff as the formatter

1. **File → Settings → Tools → Ruff** (install the Ruff plugin first if missing: **Plugins → Marketplace → search "Ruff"**)
2. Enable **Use Ruff formatter**
3. Enable **Run ruff on save** (optional but recommended)

### Step 7 — Verify setup

Run the tests using the green play button next to any test function, or from the terminal:

```bash
poetry run pytest tests/
```

---

## Running Tests

```bash
# Run all tests
poetry run pytest tests/

# Run with verbose output
poetry run pytest tests/ -v

# Run a specific test file
poetry run pytest tests/test_nlp.py
```

---

## Linting & Formatting

This project uses [Ruff](https://docs.astral.sh/ruff/) for both linting and formatting.

```bash
# Check for lint errors
poetry run ruff check .

# Auto-fix lint errors
poetry run ruff check . --fix

# Check formatting
poetry run ruff format --check .

# Apply formatting
poetry run ruff format .
```

---

## Running the Docs Site

Documentation is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

```bash
# Serve docs locally (hot-reload)
poetry run mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

```bash
# Build static site
poetry run mkdocs build
```

---

## Project Structure

```
ai-learning/
├── src/
│   └── ai_learning/        # Main package
│       ├── __init__.py
│       └── nlp/            # NLP modules
│           └── __init__.py
├── tests/                  # Pytest test files
├── docs/                   # MkDocs documentation source
│   └── index.md
├── site/                   # Built MkDocs site (generated)
├── .github/
│   └── workflows/
│       └── main.yml        # CI: runs pytest + ruff on push/PR
├── .venv/                  # Poetry virtual environment (local)
├── mkdocs.yml              # MkDocs configuration
├── pyproject.toml          # Project metadata and dependencies
└── README.md
```

---

## Topics Covered

| Topic | Description |
|-------|-------------|
| **NLP Basics** | Tokenization, stemming, lemmatization, POS tagging |
| **Text Processing** | Cleaning, normalization, stop word removal |
| **Language Models** | N-grams, perplexity, language model evaluation |
| **LLM Concepts** | Transformers, attention mechanism, fine-tuning |
| **Libraries** | NLTK, and more to be added |

---

## CI/CD

GitHub Actions runs automatically on every push and pull request to `main`:

- Installs dependencies via Poetry
- Runs `pytest` test suite
- Runs `ruff check` for lint
- Runs `ruff format --check` for formatting

See [`.github/workflows/main.yml`](.github/workflows/main.yml) for the full pipeline.
