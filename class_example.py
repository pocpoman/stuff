from test import check_credit_card

class market:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.users = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        return

    def show_items(self):
        for item in self.items:
            item.print_item()
        print()
    
    def check_items_id(self, item_for_check):
        for n in self.items:
            if item_for_check == str(n.id):
                return n
        print(f"Couldn't find item {item_for_check}")
        print()
        return None


class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        self.purchases = 0

    def print_item(self):
        print(f"{self.id} {self.name}")


    def print_cart_items(self,list_):
        space =  (17  - len(self.name)) * " "
        if self.name in list_:
            return
        else:
            list_.append(self.name)
            print(f"  {self.id}    {self.purchases}        {self.name}{space}{self.price * self.purchases}")    

class cart:
    def __init__(self, name):
        self.items = []
        self.total_price = 0
        self.name = name

    def add_item(self, item):
        if item == None:
            return
        self.items.append(item)
        self.total_price += item.price
        item.purchases += 1
        

        return
    
    def remove_item(self, item_id):
        for item in self.items:
            if str(item.id) == item_id:
                item.purchases -= 1
                self.total_price -= item.price
                self.items.remove(item)

                break
        return

    
    def show_cart_items(self):        
        list_ = []
        print(" id | amount |    name    |  total cost ")
        for item in self.items:
            item.print_cart_items(list_)
        print()
        print("total price: ",self.total_price)
        yu = input("1: exit shop, 2: remove items: ")
        return yu
    
    def checkout(self):
        if self.total_price == 0:
            print("please choose an item before you pay:")
            return
        print("total cost is ",self.total_price)
        credit_card_num = list(input("enter Card number: "))
        input("enter Cardholder Name: ")
        input("enter Expiry Date: ")
        input("enter Security Code: ")
        input("enter Billing Address: ")
        check_credit_card(credit_card_num)
        print("the package will get shiped in three years from two years ago")
        exit()
        return

items_list = [
    Item(1,"T-shirt", 34),
    Item(2, "Laptop", 800),
    Item(3, "Smartphone", 500),
    Item(4, "Headphones", 50),
    Item(5, "Backpack", 30),
    Item(6, "Water Bottle", 5),
    Item(7, "Notebook", 10),
    Item(8, "Sneakers", 70),
    Item(9, "Sunglasses", 25),
    Item(10, "Jeans", 45),
    Item(11, "Watch", 120),
    Item(12, "Coffee Mug", 8),
    Item(13, "Umbrella", 15),
    Item(14, "Fitness Tracker", 60),
    Item(15, "Bluetooth Speaker", 40),
    Item(16, "Desk Chair", 100),
    Item(17, "Desk Lamp", 25),
    Item(18, "Yoga Mat", 15),
    Item(19, "Running Shoes", 65),
    Item(20, "Dumbbell Set", 50),
    Item(21, "Cookware Set", 80),
    Item(22, "Bed Sheets", 30),
    Item(23, "Toothbrush", 5),
    Item(24, "Couch", 300),
    Item(25, "Wall Art", 40)
]

mama = market("mama")
for i in items_list:
    mama.add_item(i)


my_cart = cart("tsur")
while True:
    menu = input("1:choose item, 2:show cart, 3:pay, 4:exit shop: ")
    print()
    if menu == "1":
        v = None
        mama.show_items()
        while v != "stop":
            selected_item = input("choose an item id:")
            
            if selected_item == "stop":
                break
            v = mama.check_items_id(selected_item)
            my_cart.add_item(v)
        print()
    if menu == "2":
        cart_menu = my_cart.show_cart_items()
        if cart_menu == "1":
            continue
        elif cart_menu == "2":
            remv_item = 0
            while remv_item != "stop":        
                remv_item = input("select item id:")
                stop = my_cart.remove_item(remv_item)
            print()

    if menu == "3":
        my_cart.checkout()

    if menu == "4":
        break



