class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'hi my name is {self.name} and my age is {self.age}')


d = Dog('fred', 15)
d1 = Dog('bob', 10)
d2 = Dog('blah', 3)

d.show()
d1.show()
d2.show()
