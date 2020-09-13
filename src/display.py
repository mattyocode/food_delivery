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
                print("Great! Here's our menu:")
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
#        self.make_choice()        
                
    def make_choice(self):
        answer = str(input("Please enter number of the first item you\'d like to order:  "))
        while answer != 'done':
            if self.has_quant(answer):
                id_num, quant = self.get_quant(answer)
            else:
                id_num, quant = answer.strip(), 1
            for k, v in self.menu.menu_as_dict().items():
                if id_num == v['id']:
                    self.add_to_basket(v["id"], quant)
                    print('You have added {} x {} - £{:.2f}'.format(quant, v['description'], (v['price'] * quant) )) 
            answer = str(input("Please enter your next item, or enter done to finish: "))
        return self.basket._order

    def has_quant(self, answer):
        if 'x' in answer:
            return True

    def get_quant(self, answer):
        id_num, quant = answer.split("x")
        id_num, quant = id_num.strip(), int(quant.strip())
        return id_num, quant

    def add_to_basket(self, item, quant=1):
        if self.basket == None:
            self.basket = Basket(self.menu)
        return self.basket.add(item, quant)
        
    def clear(self):
        self.menu = None
        self.basket = None



if __name__ == "__main__":
    menu = Menu(file='menu_items.json')
    d = Display(menu)
    d.greeting()