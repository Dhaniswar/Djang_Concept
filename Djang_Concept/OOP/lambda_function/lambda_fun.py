greet = lambda : print("Hello World I am Lambda function. And some call me Anonymous function")
greet()


greet_user = lambda name : print("Hy there,", name)
greet_user("Dhaniswar")


reverse_upper = lambda string : string.upper()[::-1]
print(reverse_upper("dhaniswar"))

max_value = lambda a,b : a if (a>b) else b
print(max_value(4,9))


min_value = lambda a,b : a if (b>a) else b
print(min_value(6 , 8))


largest_number = lambda a, b, c : a if(a>b) and (a>c) else b if(b>a) and (b>c) else c
print(largest_number(50, 80, 90))



def cal_largest_number(a, b, c):
    if(a>b) and (a>c):
        return a
    
    elif (b>a) and (b>c):
        return b
    
    else:
        return c

print(cal_largest_number(40,50,60))


second_largest_num_lambda = lambda a, b , c: a if (a<b) and (a>c) else b if(b<a) and (b>c) else c

print(second_largest_num_lambda(50,3,7))

def second_largest_number(a, b, c):
    if (a<b) and (a>c):
        return a
    
    elif (a>b) and (b>c):
        return b
        
    else:
        return c

print(second_largest_number(80, 32, 40))


#python map function

def square(a):
    return a**2
    
given_number = map(square, [1,2,3,4,5,6,7,8,9,10])
print("Square number of list using map",list(given_number))
print("Square number of list using map")
for square_number_of_list in given_number:
    print(square_number_of_list)


cal_square = lambda a : a ** 2
square_of_list = list(map(cal_square, [1,2,3,4,5,6,7,8,9,10]))
print("Suare of list element :", square_of_list)



calc_voting_age = lambda num : num >= 18
voting_age_list = list(filter(calc_voting_age, [10,12,23,45,18,22,33,44,25,61,17,33]))
print("voting list ages :", voting_age_list)


from functools import reduce

cal_sum_of_list_element = lambda a, b : a + b
sum_of_list_element = reduce(cal_sum_of_list_element, [1,2,3,4,5,6,7,8,9,10])
print("the sum of first 10 numbers is :", sum_of_list_element)


def sum_of_natural_num(a):
    addition = 0
    for i in range(1, a+1):
        addition +=i
    return addition

print("sum is :", sum_of_natural_num(int(20)))

#filter with lambda function
cal_even = list(filter(lambda a : a % 2 == 0 , [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
print("list of even number => ", cal_even)


#reduce with map
cal_sum_of_list_element = reduce(lambda a, b: a + b, [1,2,3,4,5,6,7,8,9,10])
print("sum of first 10 numbers using reduce and lambda :",cal_sum_of_list_element)

