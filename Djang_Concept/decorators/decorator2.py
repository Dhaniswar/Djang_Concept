def first():

    def second():
        print("I am second inner function of first function")
    
    second()

result = first

result()