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
        if self.__items != '':
            return self.__items["reg-cod"]
        else:
            return "No menu set"

    def neat_print(self):
        

    def print_id(self):
        pass
