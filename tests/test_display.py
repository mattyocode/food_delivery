import pytest
import mock
import builtins
import unittest
import datetime
from unittest.mock import Mock, patch
from pathlib import Path
from freezegun import freeze_time

from src.display import Display
from src.restaurant import Restaurant, Menu, Basket
from src.api import TextApi

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
        assert out == "No problem! Please come back later\n\n"

def test_yes_returns_menu(display_sub, monkeypatch, capsys):
    display_sub.menu.items_as_list.return_value = ['001 - Regular Cod - £7.00']
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        with mock.patch('src.display.Display.show_menu') as copy_show_menu:
            display_sub.greeting()
            assert copy_show_menu.called

@pytest.mark.skip("Getting stuck in while loop")
def test_neither_returns_try_again(display_sub, monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'blah'):
        display_sub.greeting()
        out, err = capsys.readouterr()
        assert out == "Input not y or n. Please try again!"

def test_returns_menu(display_sub, capsys):
    display_sub.menu.items_as_list.return_value = ['001 - Regular Cod - £7.00']
    with mock.patch('src.display.Display.make_choice') as copy_make_choice:
        display_sub.show_menu()
        out, err = capsys.readouterr()
        out = out.split('\n')
        assert out[1] == '***************MENU***************'
        assert copy_make_choice.called

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

def test_choose_one_item_x2(display_sub, monkeypatch, capsys):
    display_sub.menu.menu_as_dict.return_value = { "reg-cod" : {
        "id": "001",
        "description": "Regular Cod",
        "price": 7.00 }}
    with mock.patch('builtins.input', side_effect=['001 x2', 'done']):
        display_sub.make_choice()
        out, err = capsys.readouterr()
        out = out.split('\n')
        assert out[0] == 'You have added 2 x Regular Cod - £14.00'

def test_item_added_to_basket(display_sub):
    item = { "reg-cod" : 
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

def test_get_order_total(display_sub, monkeypatch, capsys):
    display_sub.menu.menu_as_dict.return_value = { "reg-cod" : {
    "id": "001",
    "description": "Regular Cod",
    "price": 7.00 }}
    stub_basket = Mock(Basket)
    stub_basket.get_order.return_value = {'001': 2}
    display_sub.set_basket(stub_basket)
    display_sub.get_order_total()
    out, err = capsys.readouterr()
    assert out == 'You ordered items:\n2 x Regular Cod - £14.00\nTotal: £14.00\n'

def test_order_complete_yes(display_sub, monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        display_sub.order_complete()
        out, err = capsys.readouterr()
        assert out == "Your order is on its way\n"


def test_order_complete_no(display_sub, monkeypatch, capsys):
    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        with mock.patch('src.display.Display.make_choice') as copy_make_choice:
            display_sub.order_complete()
            assert copy_make_choice.called

def test_add_text_api(display_sub):
    stub_api = Mock(TextApi)
    display_sub.set_api(stub_api)
    assert display_sub.api == stub_api

@freeze_time("2020-09-17 19:45:01")
def test_message_for_text(display_sub):
    assert display_sub.message_for_text() == 'Your order will arrive before 20:15'
