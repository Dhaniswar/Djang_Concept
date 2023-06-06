class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter +=1

    def greet(self):
        return f"Hi, it's {self.name}"

    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 22)

p = Person("Hari", 1)
p1 = p.create_anonymous()
print(p1.name, p1.age)

p2 = Person.create_anonymous()
print(p2.name)