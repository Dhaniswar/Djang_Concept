class Person:

    #Parameterized constructor

    def __init__(self, name, age):

        #instance variables
        self.name = name
        self.age = age
        print("name and age of the person is {}, {}" .format(self.name, self.age))


p1 = Person("Hari", 22)

