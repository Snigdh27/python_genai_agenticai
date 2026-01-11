flavours = ["Ginger","Out of Stock","Lemon","Discontinued","Mint"]
for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"Available flavour: {flavour}")