import restaurant

class Display:

    def __init__(self):
        pass

    def greeting(self):

        while True:
            answer = input("Hello, would you like to see a menu? y/n:> ")
            if answer not in ('y', 'n'):
                print("Didn't understand. Please try again!")
                continue
            else:
                if answer == "n":
                    return "No problem!"
                elif answer == "y":
                    return "Great! Here's our menu: "

    # def show_menu(self, restaurant):
        