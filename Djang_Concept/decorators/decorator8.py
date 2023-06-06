def display_info(function):

    def calc(name, age):
        print("Arguments passed are: {0}, {1}".format(name, age))
        function(name, age)
    return calc


@display_info
def introduction(name, age):
    print('So, {name} is {age} years old and she is a {occupation}'.format(name = name, age = age, occupation = 'programmer'))
introduction("Ram",24)
