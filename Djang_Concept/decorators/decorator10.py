def umbrella_function(function):
   
    def inner_function(args1, args2):   
        print("The first argument is: {0}".format(args1))     
        function(args1, args2)
    return inner_function

def umbrella_function2(function):

    def inner_function(args1, args2):   
        print("The second argument passed is: {0}".format(args2))     
        function(args1, args2)
    return inner_function


@umbrella_function
@umbrella_function2
def another_function(name, age):
   print ('So, {name} is {age} years old and she is a {occupation}'
   .format(name = name, age = age, occupation = 'programmer'))

another_function('Mia', 18)