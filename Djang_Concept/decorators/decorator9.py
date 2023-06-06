import functools


def umbrella_function(function):
    """I am the umbrella function """
    @functools.wraps(function)    
    def inner_function(args1, args2):  
        """Inner docs""" 
        print("Arguments passed are: {0}, {1}".format(args1,args2))     
        function(args1, args2)
    return inner_function

@umbrella_function
def another_function(name, age):
    """I am the another function """
    print('So, {name} is {age} years old and she is a {occupation}'
   .format(name = name, age = age, occupation = 'programmer'))

# another_function("Kishowar", 35)

print(another_function.__name__)
print(another_function.__doc__)
print(umbrella_function.__doc__)



