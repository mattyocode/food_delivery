from src.restaurant import Restaurant, Menu, Basket


class Display:

    def __init__(self, menu=None):
        self.menu = menu
        self.basket = None

    def set_menu(self, menu):
        self.menu = menu

    def set_basket(self, basket=None):
        if self.basket == None and basket != None:
            self.basket = basket
        elif self.basket != None and basket == None:
            print("You alreedy have a basket!")
        else:
            self.basket = Basket(self.menu)

    def greeting(self):
        while True:
            answer = str(input("Hello, would you like to see a menu? y/n:> ")).lower()
            if answer == "n":
                print("No problem! Please come back later\n")
                break
            elif answer == "y":
                print('')
                print("Great! Here's our menu:")
                self.show_menu()
                break
            else:
                print("Input not y or n. Please try again!")
                continue

    def show_menu(self):
        if self.menu != None:
            print('')
            print('*' * 15 + 'MENU' + '*' * 15)
            print('')
            item_lst = self.menu.items_as_list()
            for i in item_lst:
                print(i)
        self.make_choice()        
                
    def make_choice(self):
        answer = str(input("Please enter number of the item you\'d like to order:  "))
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
        return self.get_order_total()
        

    def has_quant(self, answer):
        if 'x' in answer:
            return True

    def get_quant(self, answer):
        id_num, quant = answer.split("x")
        id_num, quant = id_num.strip(), int(quant.strip())
        return id_num, quant

    def add_to_basket(self, item, quant=1):
        if self.basket == None:
            self.set_basket() 
        return self.basket.add(item, quant)

    def get_order_total(self):
        sub_total = 0
        print("You ordered items:")
        for k, v in self.basket.get_order().items():
            for val in self.menu.menu_as_dict().values():
                if k == val["id"]:
                    item_total = (v * val["price"])
                    sub_total += item_total
                    print("{} x {} - £{:.2f}".format(v, val["description"], item_total))
        print("Total: £{:.2f}".format(sub_total))

    def order_complete(self):
        ans = ""
        while ans not in ('y', 'n'):
            ans = input("Order complete? y/n: ")
            if ans == 'y':
                print("Your order is on its way")
                break
            if ans == 'n':
                print("No problem!")
                self.make_choice()

    def clear(self):
        self.menu = None
        self.basket = None


if __name__ == "__main__":
    menu = Menu(file='menu_items.json')
    d = Display(menu)
    d.greeting()