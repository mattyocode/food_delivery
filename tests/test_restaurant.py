import pytest
from restaurant import *

f = 'menu_items.json'
subject = Menu(name="Chips")

def test_menu_returns_dictionary():
    assert subject.get_menu() == {}

# def test_get_item_id_num():
#     assert subject.

def test_get_first_menu_item():
    subject.set_menu(f)
    assert subject.print_menu() == {'id': '001', 'description': 'regular cod', 'price': 7}

# def test_neat_print():
#     subject.set_menu(f)    