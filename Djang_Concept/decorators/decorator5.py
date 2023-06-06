def umbrella_function(function):
   
    name = 'Mia Roberts'
    def inner_function():
        print(name)
        function()
    return inner_function

def another_function():
    print('I am a computer science student')

x = umbrella_function(another_function)

x()