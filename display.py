import restaurant

def greeting():
    answer = input("Hello, would you like to see a menu? y/n")
    while True:
        if answer == "n":
            return "No problem!"
            break
        elif answer == "y":
            return "Great! Here's our menu: "
            break
        else:
            return "Please try again!"
