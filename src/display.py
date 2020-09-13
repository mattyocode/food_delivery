from src.restaurant import Restaurant, Menu, Basket

class Display:

    def __init__(self, menu=None):
        self.menu = menu
        self.basket = None

    def set_menu(self, menu):
        self.menu = menu

    def greeting(self):
        while True:
            answer = str(input("Hello, would you like to see a menu? y/n:> ")).lower()
            if answer == "n":
                print("No problem! Please come back later")
                break
            elif answer == "y":
                print("Great! Here's our menu: ")
                self.show_menu()
                break
            else:
                print("Input not y or n. Please try again!")
                continue

    def show_menu(self):
        if self.menu != None:
            print('*' * 15 + 'MENU' + '*' * 15)
            item_lst = self.menu.items_as_list()
            for i in item_lst:
                print(i)

    def make_choice(self):
        answer = str(input("Please enter number of food you\'d like to order:  "))
        for k, v in self.menu.menu_as_dict().items():
            if answer == v['id']:
                self.add_to_basket(v["id"])
                print('You have added 1 x {} - £{:.2f}'.format(v['description'], v['price'])) 
            else:
                print('Not found')

    def add_to_basket(self, item):
        if self.basket == None:
            self.basket = Basket(self.menu)
        return self.basket.add(item)
        



# if __name__ == "__main__":
#     menu = Menu(file='menu_items.json')
#     d = Display(menu)
#     d.greeting()