# chai="Ginger chai"

# def prepare_chai(order):
#     print("Preparing ",order)

# prepare_chai(chai)

chai=[1,2,3]

def edit_chai(cup):
    cup[1]=42

edit_chai(chai)
print(chai)

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Ginger","Full Cream","2 spoons")
make_chai(sugar="2 spoons",milk="Full Cream",tea="Ginger")

def special_chai(*ingredients,**extras):
    print("ingredients",ingredients)
    print("extras",extras)

special_chai("Ginger","Elaichi",milk="Full Cream",sugar="2 spoons")