class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print(f"Person created, his name: {name}, surname: {surname}, age: {age}")

    def says_hello(self):
        print(f"{self.name} {self.surname} says HELLO!")


p1 = Human('Tom', 'Rider', 27)
p1.says_hello()


class Student(Human):
    def __init__(self, name, surname, age, average_grade):
        # Human.__init__(self, name, surname, age)  функция super() еквивалентна с вызовом обьекта предков
        # возвращает обьект родительского класса
        super().__init__(name, surname, age)
        self.avarage_grade = average_grade
        print(f"His name {self.name}, his surname {self.surname}, his age {self.age} and he COOL!!!")
        print(f"{self.name} have average_grade {self.avarage_grade}")

    def study(self):
        print(f'{self.name} studies')

    def says_hello(self):
        super().says_hello()
        print(f"{self.name} says hello everybody!!")


s1 = Student('Vlad', "Askarov", 26, 100)
s1.says_hello()


class Teacher(Human):
    def teach(self):
        print(f"{self.name} teaches")


t1 = Teacher('Lesia', 'Kuznetsova', 25)
t1.says_hello()
t1.surname = 'Askarova'
t1.says_hello()
s1.study()
t1.teach()

def introduce(human):
    print("Now people says HELLO!")
    human.says_hello()
people_arr = [Student('Vlad', "Askarov", 26, 100), Student('Lesia', "Askarova", 25, 80), Student("Alex", "Bogdanov", 33, 25)]
for human in people_arr:
    introduce(human)
