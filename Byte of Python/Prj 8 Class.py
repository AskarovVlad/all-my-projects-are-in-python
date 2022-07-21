# class Car:
#     def __init__(self):
#         print ("Двигатель заведен")
#         self.name = "corolla"
#         self.__make = "toyota"
#         self._model = 1999
#
#
# class Car:
#    def start(self, a, b=None):
#         if b is not None:
#             print(a + b)
#         else:
#             print(a)
# car1 = Car()
# car1.start(10)
# car1.start(10, 20)

class Vehicle:
    def print_details(self):
        print("Это родительский метод из класса Vehicle")

# создание класса, который наследует Vehicle
class Car(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Car")

# создание класса Cycle, который наследует Vehicle
class Cycle(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Cycle")

car1 = Vehicle()
car1.print_details()
car2 = Car()
car2.print_details()
car3 = Cycle()
car3.print_details()
