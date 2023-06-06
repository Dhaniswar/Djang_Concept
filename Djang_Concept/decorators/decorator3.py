def umbrella_function():
   
    name = 'Mia Roberts'
    def inner_function():
        print(name)
    # return a function
    return inner_function

x = umbrella_function()

# calling the function via a variable
x()