class A:
    label = "A: Base Class"

class B(A):
    label = "B: Masala Blend"

class C(A):
    label = "C: Herbal Blend"

class D(B,C):
    pass

cup = D()
print(cup.label)  # Output: B: Masala Blend
print(D.__mro__)  # Output: (<class '__main__.D'>, <