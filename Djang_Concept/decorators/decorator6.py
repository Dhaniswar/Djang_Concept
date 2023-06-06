def umbrella_function(function):
   
    name = 'Mia Roberts'
    def inner_function():
        print(name)
        function()
    return inner_function

@umbrella_function
def another_function():
    print('I am a computer science student')

another_function()
