class ChaiOrder:
    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai ordered."

order = ChaiOrder("Masala", 200)
print(order.summary())  # Output: 200ml of Masala chai ordered. 

order_two = ChaiOrder("Ginger", 150)
print(order_two.summary())  # Output: 150ml of Ginger chai ordered.