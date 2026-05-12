# claude_ka_saamaan

A Python project with a terminal management utility for running and logging PowerShell commands on Windows.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.env` and set your environment variables:

```
APP_NAME=claude_ka_saamaan
DEBUG=True
```

## Usage

```powershell
# Run the app
python main.py

# Run the terminal manager (executes PowerShell commands and logs to terminal_audit.log)
python terminal_manager.py
```

## Testing

```powershell
# Run all tests
python -m pytest tests/

# Run a single test
python -m pytest tests/test_utils.py::test_greet
```

## Project Structure

```
main.py              # Entry point
terminal_manager.py  # PowerShell command runner with logging
src/
  utils.py           # Shared utility functions
tests/               # pytest test suite
```
