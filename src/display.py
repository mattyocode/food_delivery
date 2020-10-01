import datetime

from src.restaurant import Restaurant, Menu, Basket
from src.api import TextApi

class Display:

    def __init__(self, menu=None):
        self._menu = menu
        self._basket = None
        self._api = TextApi()

    def set_menu(self, menu):
        self._menu = menu

    def set_basket(self, basket=None):
        if self._basket == None and basket != None:
            self._basket = basket
        elif self._basket != None and basket == None:
            print("You already have a basket!")
        else:
            self._basket = Basket(self._menu)

    def set_api(self, api):
        self._api = api
        return self._api

    def greeting(self):
        while True:
            answer = str(input("Hello, would you like to see a menu? y/n:> ")).lower()
            if answer == "n":
                print("No problem! Please come back later\n")
                break
            elif answer == "y":
                print("\nGreat! Here's our menu:")
                return self.show_menu()
            else:
                print("Input not y or n. Please try again!")

    def show_menu(self):
        if self._menu != None:
            print('\n' + '*' * 15 + 'MENU' + '*' * 15 + '\n')
            item_list = self._menu.items_as_list()
            for i in item_list:
                print(i)
        return self.make_choice()        
                
    def make_choice(self):
        answer = str(input("Please enter number of the item you\'d like to order:  "))
        while answer != 'done':
            if self.has_quant(answer):
                id_num, quant = self.get_quant(answer)
            else:
                id_num, quant = answer.strip(), 1
            for k, v in self._menu.menu_as_dict().items():
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
        if self._basket == None:
            self.set_basket() 
        return self._basket.add(item, quant)

    def get_order_total(self):
        sub_total = 0
        print("You ordered items:")
        for k, v in self._basket.get_order().items():
            for val in self._menu.menu_as_dict().values():
                if k == val["id"]:
                    item_total = (v * val["price"])
                    sub_total += item_total
                    print("{} x {} - £{:.2f}".format(v, val["description"], item_total))
        print("Total: £{:.2f}".format(sub_total))
        self.order_complete()

    def order_complete(self):
        ans = ""
        while ans not in ('y', 'n'):
            ans = input("Order complete? y/n: ")
            if ans == 'y':
                print("Your order is on its way")
                return self.send_message()
            if ans == 'n':
                print("No problem!")
                return self.make_choice()
    
    def message_for_text(self):
        now = datetime.datetime.now()
        now_plus_30 = now + datetime.timedelta(minutes = 30)
        time = now_plus_30.strftime("%H:%M")
        return f'Your order will arrive before {time}'

    def send_message(self):
        message = self.message_for_text()
        self._api.send_message(message=message)
        return 'Message sent'

    def clear(self):
        self._menu = None
        self._basket = None
        
if __name__ == "__main__":
    menu = Menu(file='menu_items.json')
    d = Display(menu)
    d.greeting()