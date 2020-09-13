import pytest
import mock
import builtins
from unittest.mock import Mock
from pathlib import Path

from src.display import Display
from src.restaurant import Restaurant, Menu

# data_folder = Path("/data")
# f = data_folder / "menu_items.json"

f = 'menu_items.json'
subject = Display()
r = Restaurant("Chipps")
stub_menu = Mock(Menu(r, f))

def test_no_returns_message(monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        subject.greeting()
        out, err = capsys.readouterr()
        assert out == "No problem! Please come back later\n"

def test_yes_returns_menu(monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        subject.greeting()
        out, err = capsys.readouterr()
        assert out == "Great! Here's our menu: \n"

@pytest.mark.skip
def test_neither_returns_try_again(monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'blah'):
        subject.greeting()
        out, err = capsys.readouterr()
        assert out == "Input not y or n. Please try again!"

def test_returns_menu(capsys):
    stub_menu.items_as_list.return_value = ['001 - Regular Cod - £7.00']
    subject.set_menu(stub_menu)
    subject.show_menu()
    captured = capsys.readouterr()
    assert captured.out == '***************MENU***************\n001 - Regular Cod - £7.00\n'

def test_choose_one_item(monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: '001'):
        stub_menu.menu_as_dict.return_value = { "reg-cod" : {
        "id": "001",
        "description": "Regular Cod",
        "price": 7.00 }}
        subject.set_menu(stub_menu)
        subject.make_choice()
        out, err = capsys.readouterr()
        assert out == 'You have added 1 x Regular Cod - £7.00\n'

def test_item_added_to_basket():
    item = { 
    "reg-cod" : 
    {"id": "001",
    "description": "Regular Cod",
    "price": 7.00 }}
    expected = 1
    subject.set_menu(stub_menu)
    assert subject.add_to_basket(item) == expected

    