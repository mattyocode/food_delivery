import config

class Menu:

    def __init__(self, items={}):
        self.items = items

    def get_menu(self):
        return self.items