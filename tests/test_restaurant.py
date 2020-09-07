import pytest
from src.restaurant import Restaurant, Menu

f = 'menu_items.json'

@pytest.fixture
def subject():
    r = Restaurant("Chipppz")
    subject = Menu(r)
    yield subject
    subject.clear()

def test_restaurant_returns_name(subject):
    name = "Chips"
    r = Restaurant(name)
    assert r.get_name() == "Chips"

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