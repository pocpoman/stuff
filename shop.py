import json


def show_items(stuff):
    
    for i in stuff:
        print(i["id"], i["name"], i["cost"])
        


def menu_(stuff,item_id):
    print()
    menu = input("1:choose item, 2:show cart, 3:pay: ")
    while menu != "exit":
        if menu == "1":
            while item_id != "exit":
                item_id = input("type item number: ")
                for i in stuff:
                    if item_id == str(i["id"]):
                        cart.append(i)
                        break
            else:
                return item, menu
        
        elif menu == "2":
            print()
            show_items(cart)
            cart_items = input("1:remove items, 2:exit cart")
            if cart_items == "1":
                removed_num = 0
                while removed_num != "exit":
                    removed_num = input("type item number you want to remove: ")
                    for n in cart:
                        if  removed_num == str(n["id"]):
                            cart.remove(n)
                            break
            return item, menu
        

        elif menu == "3":
            print()
            total_cost = 0
            for c in cart:
                total_cost = total_cost + c["cost"]
                if total_cost == 0:
                    print("please choose an item before you pay:")
            print("total cost is ",total_cost)
            input("enter Card number: ")
            input("enter Cardholder Name: ")
            input("enter Expiry Date: ")
            input("enter Security Code: ")
            input("enter Billing Address: ")
            break

    return item, menu
    
    
            



cart = [] 
_items_ = [
        { "id":1, "name": "t-shirt", "cost":34},

        { "name":"sweatshirt", "id":2, "cost":50},

        {"name": "pants", "id":3,  "cost":41},

        {"name":"pistol", "id":4, "cost":654},

        {"name": "15x9mm bullet" ,"id":5, "cost":4.5}
        ]
item = None
true_or_false = None
show = None
menu = None

print("welcome to shop:")
show = input("show items: ")
while show or menu != "exit":
    
    
    if show == "yes":
        show_items(_items_)
        while menu != "exit":
            true_or_false, menu = menu_(_items_,item)
            if menu == "3":
                exit()
            
        

        






