import sys
import pytest
from ..src.view.view import CLI
from unittest.mock import MagicMock
import builtins


@pytest.fixture
def cli() -> CLI:
    mock_model = MagicMock()
    mock_model._gues_range.min = 1
    mock_model._gues_range.max = 10
    mock_controller = MagicMock()
    mock_controller._model = mock_model
    v = CLI()
    v.setup_controller(mock_controller)
    return v


def test_display_message(cli, capsys):
    cli.display_message("test")
    captured = capsys.readouterr()
    assert captured.out == "test\n"


def test_get_user_input(cli, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda: "1")
    cli.get_user_input()
    assert cli._user_eingabe == 1


def test_get_user_input_fail_out_of_range(cli, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda: "165")
    with pytest.raises(ValueError):
        cli.try_user_value()


def test_get_user_input_fail_no_number(cli, monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda: "A")
    with pytest.raises(ValueError):
        cli.try_user_value()
