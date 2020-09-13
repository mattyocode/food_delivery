import pytest
from pathlib import Path
from src.restaurant import Restaurant, Menu, Basket

f = "menu_items.json"

@pytest.fixture
def subject():
    r = Restaurant("Chipppz")
    subject = Menu(r)
    yield subject
    subject.clear()

#Tests for Restaurant class
    
def test_restaurant_returns_name():
    name = "Chips"
    r = Restaurant(name)
    assert r.get_name() == "Chips"

#Tests for Menu class

def test_menu_returns_name(subject):
    assert subject.which_restaurant() == subject._restaurant.get_name()

def test_menu_as_dict_returns_items_attribute(subject):
    menu_items = subject.set_menu(f)
    assert menu_items == subject._items

def test_get_first_menu_item(subject):
    subject.set_menu(f)
    assert subject.items_as_list()[0] == '001 - Regular Cod - £7.00\n'

def test_menu_list_third_item(subject):
    subject.set_menu(f)
    assert subject.items_as_list()[2] == '003 - Scampi - £6.50\n'

def test_list_with_no_menu_set_raises_error(subject):
    with pytest.raises(TypeError, match="No menu added yet"):
        subject.items_as_list()

#Tests for Basket class

def test_add_1_item(subject):
    b = Basket(subject)
    assert b.add('001') == 1
    assert b._order == {'001': 1}

def test_add_2_of_same_item(subject):
    b = Basket(subject)
    assert b.add('001', 2) == 2
    assert b._order == {'001': 2}

def test_add_2_different_items(subject):
    subject.set_menu(f)
    b = Basket(subject)
    b.add('001')
    b.add('002')
    assert b._order == {'001': 1, '002': 1}

def test_add_2_items_different_quanitity(subject):
    subject.set_menu(f)
    b = Basket(subject)
    b.add('001')
    b.add('002', 2)
    assert b._order == {'001': 1, '002': 2}

def test_total_cost_updated(subject):
    subject.set_menu(f)
    b = Basket(subject)
    assert b.increase_total('001') == 7.0

def test_total_cost_updated_2x_item(subject):
    subject.set_menu(f)
    b = Basket(subject)
    assert b.increase_total('001', 2) == 14.0

def test_total_cost_updated_2x_item_diff_quantities(subject):
    subject.set_menu(f)
    b = Basket(subject)
    b.increase_total('001', 1)
    b.increase_total('002', 2)
    expected_total = 18.4
    assert expected_total == b._total_cost

def test_get_total(subject):
    subject.set_menu(f)
    b = Basket(subject)
    assert b.get_total() == 0

