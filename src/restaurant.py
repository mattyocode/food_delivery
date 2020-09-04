import config
import json

class Menu:

    def __init__(self, name):
        self.__name = name
        self.__items= {}

    def get_menu(self):
        return self.__items

    def set_menu(self, file):
        with open(file) as json_file:
            self.__items = json.load(json_file)
        return self.__items

    def print_menu(self):
        if self.__items == {}:
            return "No menu set"
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