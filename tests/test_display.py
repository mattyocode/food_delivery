import pytest
import mock
import builtins

import display

def test_no_returns_message(monkeypatch):
    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        assert display.greeting() == "No problem!"

def test_yes_returns_menu(monkeypatch):
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert display.greeting() == "Great! Here's our menu: "


