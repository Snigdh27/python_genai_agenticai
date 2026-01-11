essential_spices = {"cardamom","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")                             

only_essential = essential_spices - optional_spices
print(f"Only essential spices: {only_essential}")

print(f"Is 'cloves' an essential spice ? {'ginger' in essential_spices}")

