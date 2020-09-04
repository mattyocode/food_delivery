import pytest
import mock
import builtins
from unittest.mock import Mock

from src.display import Display
from src.restaurant import Menu

f = 'menu_items.json'
subject = Display()
stub_menu = Mock(Menu("Chip"))

def test_no_returns_message(monkeypatch):
    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        assert subject.greeting() == "No problem!"

def test_yes_returns_menu(monkeypatch):
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert subject.greeting() == "Great! Here's our menu: "

# def test_neither_returns_try_again(monkeypatch, capsys):
#     with mock.patch.object(builtins, 'input', lambda _: 'blah'):
#         captured = capsys.readouterr()
#         assert captured.out == "Didn't understand. Please try again!\n"

def test_returns_menu(capsys):
    stub_menu.print_menu.return_value = ['001 - Regular Cod - £7.00', '002 - Small Cod - £5.70', '003 - Scampi - £6.50']
    subject.show_menu(stub_menu)
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == '***************MENU***************\n001 - Regular Cod - £7.00\n002 - Small Cod - £5.70\n003 - Scampi - £6.50\n'

# def test_ask_for_choice():
#     assert subject.make_choice() == ''