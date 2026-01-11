chai_order = dict(type="Masala Chai", size="Large", sugar = 2)
print(f"Chai order : {chai_order}")

chai_recipe = {}
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="milk"

print(f"Recipe base : {chai_recipe['base']}")
del chai_recipe["liquid"]
print(f"Chai recipe after deleting liquid : {chai_recipe}")

print(f"Is sugar in order ? {'sugar' in chai_order}")

# print(f"Order details keys : {chai_order.keys()}")
# print(f"Order details values : {chai_order.values()}")
# print(f"Order details items : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Popped item : {last_item}")
print(f"Chai order after popping last item : {chai_order}")

extra_spices = {"cardamom":"crushed","ginger":"sliced"}
chai_recipe.update(extra_spices)
print(f"Chai recipe after adding extra spices : {chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai size from order : {chai_size}")

chai_size = chai_order.get("note","NO Note")
print(f"Chai note from order : {chai_size}")