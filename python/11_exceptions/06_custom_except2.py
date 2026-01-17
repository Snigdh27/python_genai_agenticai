class OutOfIngredientError(Exception):
    pass

def make_chai(milk,sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientError("Missing milk")
    print("Chai is ready")