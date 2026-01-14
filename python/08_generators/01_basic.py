def serve_chai():
    yield "Cup1: Masala Chai"
    yield "Cup2: Ginger Chai"
    yield "Cup3: Cardamom Chai"

stall = serve_chai()

for cup in stall:
    print(cup)

#normal function
def get_chai_list():
    return ["Cup 1","Cup 2","Cup 3"]

def get_chai_get():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_get()
print(next(chai))