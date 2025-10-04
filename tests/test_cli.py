"""Tests for CLI interface."""

from click.testing import CliRunner

from food_automation.cli import main


def test_cli_requires_photo_path():
    """Test that CLI requires a photo path argument."""
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code != 0


def test_cli_rejects_nonexistent_file():
    """Test that CLI rejects non-existent file paths."""
    runner = CliRunner()
    result = runner.invoke(main, ["nonexistent.jpg"])
    assert result.exit_code != 0
