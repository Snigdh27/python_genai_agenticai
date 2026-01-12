def chai_flavour(flavour="masala"):
    """Return the flavour of chai."""
    return flavour

print(chai_flavour.__doc__ ) #docstring of function
print(chai_flavour.__name__) #name of function

def generate_bill(chai=0,samosa=0):
    """Calculate total bill."""
    total = chai*10 + samosa*20
    return total,"Thank you for visiting!"