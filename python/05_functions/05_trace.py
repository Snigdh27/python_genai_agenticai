def add_vats(price,vat_rate):
    return price*(100+vat_rate)/100

orders = [100,200,300]

for price in orders:
    final_amount = add_vats(price,15)
    print(f"Original : {price}, Final Amount : {final_amount}")