import pytest
import mock
import builtins
from unittest.mock import Mock

from src.display import Display
from src.restaurant import Restaurant, Menu

f = 'menu_items.json'
subject = Display()
r = Restaurant("Chipps")
stub_menu = Mock(Menu(r))

# def test_no_returns_message(monkeypatch):
#     with mock.patch.object(builtins, 'input', lambda _: 'n'):
#         subject.greeting()
#         out, err = capsys.readouterr()
#         assert out == "No problem!"

# def test_yes_returns_menu(monkeypatch):
#     with mock.patch.object(builtins, 'input', lambda _: 'y'):
#         assert subject.greeting() == "Great! Here's our menu: "

# def test_neither_returns_try_again(monkeypatch, capsys):
#     with mock.patch.object(builtins, 'input', lambda _: 'blah'):
        # subject.greeting()
        # out, err = capsys.readouterr()
        # assert err == ValueError


# def test_returns_menu(capsys):
#     stub_menu.print_menu.return_value = ['001 - Regular Cod - £7.00', '002 - Small Cod - £5.70', '003 - Scampi - £6.50']
#     subject.show_menu(stub_menu)
#     captured = capsys.readouterr()
#     assert captured.out == '***************MENU***************\n001 - Regular Cod - £7.00\n002 - Small Cod - £5.70\n003 - Scampi - £6.50\n'

# def test_ask_for_choice(capsys):
#     subject.make_choice()
#     out, err = capsys.readouterr()
#     assert out == 'Please enter number of food you\'d like to order:  '