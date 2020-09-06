import pytest
from src.restaurant import Restaurant, Menu

f = 'menu_items.json'

@pytest.fixture
def subject():
    r = Restaurant("Chipppz")
    subject = Menu(r)
    yield subject
    subject.clear()

def test_restaurant_returns_name():
    r = Restaurant("Chips")
    assert r.get_name() == "Chips"

def test_menu_returns_name(subject):
    assert subject.which_restaurant() == "Chipppz"

def test_menu_returns_dictionary(subject):
    subject.set_menu(f)
    assert subject.get_menu_items()["mushy-peas"] == {'description': 'Mushy Peas', 'id': '004', 'price': 2.5}

@pytest.mark.skip(reason="Need to move test to display")
def test_get_first_menu_item(subject):
    subject.set_menu(f)
    assert subject.print_menu()[0] == '001 - Regular Cod - £7.00'

@pytest.mark.skip(reason="Need to move test to display")
def test_neat_print_first_three_items(subject):
    subject.set_menu(f)
    assert subject.neat_print()[:3] == ['001 - Regular Cod - £7.00', '002 - Small Cod - £5.70', '003 - Scampi - £6.50']

@pytest.mark.skip(reason="Need to move test to display")
def test_print_with_no_menu_set(subject):
    assert subject.print_menu() == "No menu added yet"