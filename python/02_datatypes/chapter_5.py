import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.50
current_temp = 95.49

print(f"Ideal temp {ideal_temp}")
print(f"Current temp {current_temp}")
print(f"Difference: {ideal_temp - current_temp}")
print(sys.float_info)