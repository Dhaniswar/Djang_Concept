class Dog:

    #class variable
    animal = "Dog"

    # Constructor

    def __init__(self, breed):

        #instance variable inside constructor
        self.breed = breed

    
    #Normal Method
    def setColor(self, color):
        #instance variable in normal method
        self.color = color

    def getColor(self):
        return self.color
    

Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())