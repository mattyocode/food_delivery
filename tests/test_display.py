import pytest
import mock
import builtins
import unittest
from unittest.mock import Mock, patch
from pathlib import Path

from src.display import Display
from src.restaurant import Restaurant, Menu

# data_folder = Path("/data")
# f = data_folder / "menu_items.json"

@pytest.fixture
def display_sub():
    stub_menu = Mock(Menu)
    display_sub = Display(stub_menu)
    yield display_sub
    display_sub.clear()

def test_no_returns_message(display_sub, monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        display_sub.greeting()
        out, err = capsys.readouterr()
        assert out == "No problem! Please come back later\n"

def test_yes_returns_menu(display_sub, monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        display_sub.menu.items_as_list.return_value = ['001 - Regular Cod - £7.00']
        display_sub.greeting()
        out, err = capsys.readouterr()
        out = out.split('\n')
        display_sub.make_choice = None #prevent make_choice() being called
        assert out[0] == "Great! Here's our menu:"

@pytest.mark.skip
def test_neither_returns_try_again(display_sub, monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'blah'):
        display_sub.greeting()
        out, err = capsys.readouterr()
        assert out == "Input not y or n. Please try again!"

def test_returns_menu(display_sub, capsys):
    display_sub.menu.items_as_list.return_value = ['001 - Regular Cod - £7.00']
    display_sub.show_menu()
    captured = capsys.readouterr()
    assert captured.out == '***************MENU***************\n001 - Regular Cod - £7.00\n'

def test_choose_one_item(display_sub, monkeypatch, capsys):
    display_sub.menu.menu_as_dict.return_value = { "reg-cod" : {
        "id": "001",
        "description": "Regular Cod",
        "price": 7.00 }}
    with mock.patch('builtins.input', side_effect=['001', 'done']):
        display_sub.make_choice()
        out, err = capsys.readouterr()
        out = out.split('\n')
        assert out[0] == 'You have added 1 x Regular Cod - £7.00'

@pytest.mark.skip("v1 choose one item test")
def test_choose_one_item_old(display_sub, monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: '001'):
        display_sub.menu.menu_as_dict.return_value = { "reg-cod" : {
        "id": "001",
        "description": "Regular Cod",
        "price": 7.00 }}
        display_sub.make_choice()
        out, err = capsys.readouterr()
        out = out.split('\n')
        assert out[0] == 'You have added 1 x Regular Cod - £7.00\n'

@pytest.mark.skip
def test_choose_one_item_x2(display_sub, monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: '001 x2'):
        display_sub.menu.menu_as_dict.return_value = { "reg-cod" : {
        "id": "001",
        "description": "Regular Cod",
        "price": 7.00 }}
        display_sub.make_choice()
        out, err = capsys.readouterr()
        assert out == 'You have added 2 x Regular Cod - £14.00\n'

def test_item_added_to_basket(display_sub):
    item = { 
    "reg-cod" : 
    {"id": "001",
    "description": "Regular Cod",
    "price": 7.00 }}
    expected = 1
    assert display_sub.add_to_basket(item) == expected

def test_answer_contains_quantity(display_sub):
    answer = "001 x2"
    assert display_sub.has_quant(answer) == True

def test_split_answer_into_item_and_quant(display_sub):
    answer = "001 x2"
    assert display_sub.get_quant(answer) == ("001", 2)
    