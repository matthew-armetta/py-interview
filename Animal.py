class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'hi my name is {self.name} and my age is {self.age}')

    def hi(self):
        print('hi')


d = Animal('fred', 15)

d.show()
