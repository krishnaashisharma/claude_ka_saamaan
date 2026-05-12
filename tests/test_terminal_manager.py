from unittest.mock import patch, MagicMock
from terminal_manager import run_command, log_action


def test_run_command_success():
    mock_result = MagicMock(returncode=0, stdout="output", stderr="")
    with patch("terminal_manager.subprocess.run", return_value=mock_result):
        assert run_command("echo hi", "test") == "output"


def test_run_command_failure():
    mock_result = MagicMock(returncode=1, stdout="", stderr="error msg")
    with patch("terminal_manager.subprocess.run", return_value=mock_result):
        assert run_command("bad cmd", "test") == "error msg"


def test_run_command_exception():
    with patch("terminal_manager.subprocess.run", side_effect=FileNotFoundError("not found")):
        result = run_command("missing", "test")
        assert "not found" in result


def test_log_action(caplog):
    import logging
    with caplog.at_level(logging.INFO, logger="root"):
        log_action("cmd", "SUCCESS", "doing a thing")
    assert any("SUCCESS" in r.message for r in caplog.records)
