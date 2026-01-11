ingredients = ["water","milk","black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients after removing water: {ingredients}")

spice_options = ["ginger","cardamom"]
chai_ingredients = ["water","milk"]
chai_ingredients.extend(spice_options)
print(f"Chai ingredients are: {chai_ingredients}")
chai_ingredients.insert(2,"black tea")
print(f"Chai ingredients after inserting black tea: {chai_ingredients}")

last_ingredient = chai_ingredients.pop()
print(f"{last_ingredient}")
print(f"chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"Chai : {chai_ingredients}")
chai_ingredients.sort()
print(f"Chai sorted ingredients: {chai_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"Max sugar level : {max(sugar_levels)}")
print(f"Min sugar level : {min(sugar_levels)}")

base_liquid = ["water","milk"]
extra_flavour = ["ginger"]
full_liquid = base_liquid + extra_flavour
print(f"Full liquid ingredients : {full_liquid}")

strong_brew = ["black tea","water"] * 3
print(f"Strong brew ingredients : {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA",b"CARD")
print(f"Bytes : {raw_spice_data}")