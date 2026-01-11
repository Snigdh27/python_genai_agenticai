snack = input("Enter your preferred snack : ").lower()
print(f"User said : {snack}")
if snack == "cookies" or snack == "samosa":
    print("Order is confirmed")
else:
    print("We don't have that snack available")