import json


def show_items(stuff):
    x = 1
    for i in stuff:
        print(x,i,stuff[i])
        x += 1


def menu_(stuff,item):
    
    menu = input("1:choose item, 2:show cart, 3:pay, 4:home page: ")
    while item != "exit":
        if menu == "1":
            item = input("type item name: ")
            for i in stuff:
                if item == i:
                    cart[item] = item
        return item, menu
            



cart = {} 
_items_ = {"t-shirt":34,
        "sweatshirt":50,
        "pants":41,
        "pistol":654,
        "15x9mm bullet":4.5
        }
item = None
true_or_false = None
show = None
menu = None
while show or menu != "exit":
    print("welcome to shop:")
    show = input("1:show items, 2:show cart: ")
    while show or menu != "exit":
        
        
        if show == "1":
            show_items(_items_)
            while show == "1":
                true_or_false, show = menu_(_items_,item)

        






