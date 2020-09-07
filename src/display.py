import restaurant

class Display:

    def __init__(self, menu=None):
        self.menu = menu

    def greeting(self):
        while True:
            answer = str(input("Hello, would you like to see a menu? y/n:> ")).lower()
            if answer not in ('y', 'n'):
                raise ValueError("Input not y or n. Please try again!")
                continue
            else:
                if answer == "n":
                    return "No problem!"
                elif answer == "y":
                    return "Great! Here's our menu: "

    def show_menu(self, rest_menu):
        print('*' * 15 + 'MENU' + '*' * 15)
        item_list = rest_menu.print_menu()
        for i in item_list:
            print(i)

    def make_choice(self):
        answer = str(input("Please enter number of food you\'d like to order:  "))

d = Display()
d.greeting()