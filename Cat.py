from Animal import Animal


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.lives = 9

    def show(self):
        print(f'hi my name is {self.name} and my age is {self.age} and i have {self.lives} lives')


c = Cat('fred', 15)
c1 = Cat('bob', 10)
c2 = Cat('blah', 3)

c.show()
c1.show()
c2.show()
c2.hi()