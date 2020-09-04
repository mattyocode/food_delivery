import src.restaurant

class Display:

    def __init__(self):
        pass

    def greeting(self):
        while True:
            answer = str(input("Hello, would you like to see a menu? y/n:> ")).lower()
            if answer not in ('y', 'n'):
                print("Didn't understand. Please try again!")
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