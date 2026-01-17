def process_order(item,quantity):
    try:
        price = {"masala":20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be a number")

process_order("masala",2)
process_order("elaichi",2)
process_order("ginger","two")