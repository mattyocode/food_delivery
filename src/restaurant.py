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
        self.__restaurant = restaurant
        self.__items= None

    def which_restaurant(self):
        return self.__restaurant.get_name()

    def get_menu_items(self):
        return self.__items

    def set_menu(self, file):
        with open(file) as json_file:
            self.__items = json.load(json_file)
        return self.__items

    def print_menu(self):
        if self.__items == None:
            return "No menu added yet"
        else:
            return self.neat_print()

    def neat_print(self):
        menu_table = []
        for item in self.__items.values():
            menu_table.append(item['id'] + ' - ' + item['description'] + ' - £' + format(item['price'], '.2f'))
        return menu_table

    def clear(self):
        self.__name = None
        self.__items= {}