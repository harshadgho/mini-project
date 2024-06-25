menu = {
    'pizza': 150,
    'coffe': 70,
    'burger': 120,
    'salad': 80,
    'pasta': 110,
}

print("welcome to harsh restorant")
print("pizza: Rs150\npasta: Rs110\ncoffe: Rs70\nburger: Rs120\nsalad: Rs80")

order_total = 0

item_1 = input("enter the name of the order to you want")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item [item_1] to added to your order")

else:
    print(f"your item [item_1] order is not available!")


another_order =input("do you want to other item (yes/no)")
if another_order == "yes":
    item_2 = input("enter the name of second item =")
    if item_2  in menu:
        order_total +=  menu[item_2]
        print(f"item {item_2} has been added to your order")
    else:
        print(f"order item is {item_2}is not available")
print (f"the total amount of item to pay is {order_total}")
print ("thank you to connect harsh resto")

