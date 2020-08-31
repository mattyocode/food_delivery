import pytest
from restaurant import *

subject = Menu()

def test_menu_returns_dictionary():
    assert subject.get_menu() == {}