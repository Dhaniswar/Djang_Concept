



values = [1,2,3,4,5]









def multiply_element_by_one_less_than_index(numbers):
    total = 0
    for index, number in enumerate(numbers):
       total += number * (index -1)
    return total

print(multiply_element_by_one_less_than_index(values))