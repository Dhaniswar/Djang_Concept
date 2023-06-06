"""
1. The callable function accepts an object. It returns True if the object is callable. Otherwise, it returns False.
2. All built-in functions are callable. For example, print, len, even callable.
"""

# print(callable(print))
# print(callable(len))
# print(callable(sum))
# print(callable(callable))


"""
All user-defined functions created using def or lambda expressions are callable. For example:
"""

# def add(a, b):
#     return a + b

# print(callable(add))

# print(callable(lambda x: x*x))


"""
The built-in method such as a_str.upper, a_list.append are callable. For example:
"""

# str = 'Python Callable'
# print(callable(str.upper)) 

"""
If a class implements the __call__ method, all instances of the class are callable:
"""

class Counter:
    def __init__(self, start=1):
        self.count = start

    def increase(self):
        self.count += 1

    def value(self):
        return self.count

    def __call__(self):
        self.increase()


counter = Counter()
counter()

print(callable(counter))  # True