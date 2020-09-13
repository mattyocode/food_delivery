import os, json
from pathlib import Path

class Restaurant:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

class Menu:

    def __init__(self, restaurant=None, file=None):
        self._restaurant = restaurant
        self._items = self.set_menu(file) if file != None else None

    def which_restaurant(self):
        return self._restaurant.get_name()

    def set_menu(self, file):
        f = os.path.join('../src/data', file)
        with open(f) as json_file:
            self._items = json.load(json_file)
        return self._items

    def menu_as_dict(self):
        return self._items

    def items_as_list(self):
        if self._items == None:
            raise TypeError("No menu added yet")
        else:
            return self.menu_dict_to_list()

    def menu_dict_to_list(self):
        menu_table = []
        for val in self._items.values():
            menu_table.append(val['id'] + ' - ' + val['description'] + ' - £' + format(val['price'], '.2f') + '\n')
        return menu_table

    def clear(self):
        self._restaurant = None
        self._items= {}

class Basket:
    
    def __init__(self, menu=None):
        self._menu = menu
        self._order = {}
        self._total_cost = 0

    def add(self, item_id, quant=1):
        self._order[f"{item_id}"] = quant
        return self._order[f"{item_id}"]

    def increase_total(self, item_id, quant=1):
        for val in self._menu.menu_as_dict().values():
            if val["id"] == item_id:
                self._total_cost += (val["price"] * quant)
        return self._total_cost 

    def get_total(self):
        return self._total_cost




