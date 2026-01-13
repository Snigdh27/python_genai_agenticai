menu = [
    "Masala Chai",
    "iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea"
]

iced_tea = [my_tea for my_tea in menu if len(my_tea)>12]
print(iced_tea)