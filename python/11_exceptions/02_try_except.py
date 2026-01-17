chai_menu = {"masala":30, "ginger":25}

try:
    chai_menu["elaichi"]
except KeyError as e:
    print(f"Chai type not found: {e}")

print("Continuing with the rest of the program...")