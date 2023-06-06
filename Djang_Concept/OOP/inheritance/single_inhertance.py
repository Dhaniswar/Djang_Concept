class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, ti's {self.name}"

class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title
    
    def greet(self):
        return super().greet() + f" I am a {self.job_title}"
p = Employee("Ram", 22, "IT Officer")
print(p.greet())