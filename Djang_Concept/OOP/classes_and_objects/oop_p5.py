class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter +=1

    def greet(self):
        return f"Hi, it's {self.name}"
    

p1 = Person("Ram", 25)
p1 = Person("Sita", 35)
p1 = Person("Hari", 18)

print("Total no of instance of Person class created => ", Person.counter)
