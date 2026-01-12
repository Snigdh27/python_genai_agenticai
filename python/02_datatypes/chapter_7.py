masala_spices = ("cardamon","cloves","cinnamon")

(spice1,spice2,spice3)=masala_spices

print(f"Main masala spices : {spice1}, {spice2}, {spice3}")

ginger_ratip, cardamon_ratio = 2,1
print(f"Ratio is G:{ginger_ratip} and C:{cardamon_ratio}")

ginger_ratip, cardamon_ratio = cardamon_ratio,ginger_ratip
print(f"After swapping Ratio is G:{ginger_ratip} and C:{cardamon_ratio}")

print(f"Is ginger in masala spices ? {'cloves' in masala_spices}")