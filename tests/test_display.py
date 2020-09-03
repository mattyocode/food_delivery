import pytest
import mock
import builtins

import display

subject = display.Display()

def test_no_returns_message(monkeypatch):
    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        assert subject.greeting() == "No problem!"

def test_yes_returns_menu(monkeypatch):
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert subject.greeting() == "Great! Here's our menu: "

# def test_neither_returns_try_again(monkeypatch):
#     with mock.patch.object(builtins, 'input', lambda _: 'blah'):
#         assert display.greeting() == "Hello, would you like to see a menu? y/n:> "