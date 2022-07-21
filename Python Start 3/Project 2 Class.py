class Things:
    pass


class Inanimate(Things):
    pass


class Animate(Things):
    pass


class Sidewalks(Inanimate):
    pass


class Animals(Animate):
    @staticmethod
    def breathe():
        print("Дышит")

    @staticmethod
    def move():
        print("Двигается")

    @staticmethod
    def eat_food():
        print("Ест")

    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color


class Mammals(Animals):
    @staticmethod
    def feed_young_milk():
        print("Кормит детёнышей молоком")


class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print("Я нашел еду!")
        self.eat_food()

    def eat_leaves_from_trees(self):
        self.eat_food()

    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

    @staticmethod
    def left_foot_forward():
        print('левая нога впереди')

    @staticmethod
    def right_foot_forward():
        print('правая нога впереди')

    @staticmethod
    def left_foot_back():
        print('левая нога назад')

    @staticmethod
    def right_foot_back():
        print('правая нога назад')

    def dance(self):
        self.left_foot_forward()
        self.right_foot_forward()
        self.left_foot_back()
        self.right_foot_back()


ozwald = Giraffes('Гиппогриф', 6, "чорный")

ozwald.dance()
harry = Giraffes('Гиппогриф', 6, "серый")
harry.dance()
harry.find_food()
harry.eat_food()

n = 4000000
def fib(n):
    return fib(n-1) + fib(n-2)
print(fib(10))
