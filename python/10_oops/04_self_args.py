class Chaicup:
    size = 150
    
    def describe(self):
        return f"A {self.size} ml cup of chai."

cup = Chaicup()
print(cup.describe())  # Output: A 150 ml cup of chai.
print(Chaicup.describe(cup))  # Output: A 150 ml cup of chai.

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))  # Output: A 100 ml cup of chai.   