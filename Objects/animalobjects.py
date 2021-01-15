# animalobjects.py

# practice object-oriented programming
# in the context of animals

class Animal():
    #constructor
    def __init__(self):
        self.name = ""
        self.legs = 0
        print("I'm the constructor")

# creating an animal object


def talk(self):
    if self.name != "Unnamed":
        print(f"Hello, my name is, {self.name}!")
    else:
        print("Hello")
some_animal = Animal()

print(some_animal.name)

some_animal.name = "Rex"
print(some_animal.name)
some_animal.legs = 2
print(some_animal.name)

#make your own

some_other_animal = Animal()
some_other_animal.name = "lmao"
some_other_animal.legs = 20
print(f"{some_other_animal.name}\n{some_other_animal.legs}")
print(type(some_other_animal)
some_other_animal.talk()

another_animal = Animal()

another_animal