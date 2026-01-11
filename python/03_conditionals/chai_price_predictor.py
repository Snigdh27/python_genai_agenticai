chai_size = input("Enter chai size (Small/Medium/Large): ").lower()
if chai_size == "small":
    print("Chai price is Rs.10")
elif chai_size == "medium":
    print("Chai price is Rs.15")
elif chai_size == "large":
    print("Chai price is Rs.20")
else:
    print("Unknown cup size")