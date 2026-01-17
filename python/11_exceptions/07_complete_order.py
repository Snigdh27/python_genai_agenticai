class InvalidChaiError(Exception): pass

def bill(flavour,cups):
    menu = {"masala":20,"ginger":40}
    try:
        if flavour not in menu:
            raise InvalidChaiError("Chai is not available")
        if not isinstance(cups,int):
            raise TypeError("Number of cups must be integer")
        total = menu[flavour]*cups
        print(f"Your bill for {cups} ordered of {flavour} is {total}")
    except Exception as e:
        print("Error: ",e)
    finally:
        print("Thank you for visiting chai code.!")