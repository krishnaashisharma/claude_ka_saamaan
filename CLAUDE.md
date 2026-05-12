# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**claude_ka_saamaan** is a Python project. Entry point is `main.py`; shared helpers live in `src/`; tests in `tests/`.

## Environment Setup

```powershell
# Create and activate virtual environment (Windows)
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Environment variables are loaded from `.env` (see `.env` for available keys: `APP_NAME`, `DEBUG`).

## Common Commands

```powershell
# Run the app
python main.py

# Run all tests
python -m pytest tests/

# Run a single test file
python -m pytest tests/test_utils.py

# Run a single test by name
python -m pytest tests/test_utils.py::test_greet

# Run the terminal manager
python terminal_manager.py
```

## Architecture

```
main.py              # Entry point — imports from src and runs the app
terminal_manager.py  # Runs PowerShell commands non-interactively and logs results to terminal_audit.log
src/
  utils.py           # Shared utility functions
  __init__.py
tests/
  test_utils.py      # pytest tests mirroring src/ structure
  __init__.py
.env                 # Local env vars (not committed)
requirements.txt     # Runtime dependencies: python-dotenv, requests, httpx, pytest
```

`python-dotenv` is available; load `.env` with `load_dotenv()` from `dotenv` when environment variables are needed at runtime.
