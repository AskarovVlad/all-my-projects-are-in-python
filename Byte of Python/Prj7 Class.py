class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"{self.name} have a breed {self.breed}")

    def bark(self):
        print(f"{self.name} is barking")

d1 = Dog('Rex', 'husky')
d1.eat()
d1.bark()
print(d1.breed)
