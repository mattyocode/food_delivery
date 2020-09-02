import restaurant

def greeting():
    answer = input("Hello, would you like to see a menu? y/n")

    if answer == "n":
        return "No problem!"
    elif answer == "y":
        return "Great! Here's our menu: "
    else:
        return "Please try again!"
