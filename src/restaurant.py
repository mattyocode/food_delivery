import config
import json

class Restaurant:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

class Menu:

    def __init__(self, restaurant):
        self._restaurant = restaurant
        self._items= None

    def which_restaurant(self):
        return self._restaurant.get_name()

    def get_menu_items(self):
        print(self._items)
        return self._items

    def set_menu(self, file):
        with open(file) as json_file:
            self._items = json.load(json_file)
        return self._items

    def get_menu_items_as_list(self):
        if self._items == None:
            return "No menu added yet"
        else:
            return self.menu_dict_to_list()

    def menu_dict_to_list(self):
        menu_table = []
        for item in self._items.values():
            menu_table.append(item['id'] + '-' + item['description'] + '-£' + format(item['price'], '.2f'))
        return menu_table

    def clear(self):
        self._restaurant = None
        self._items= {}