### Higher Order Functions ###

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_one(first_value, second_value, f_sum):
    sum_values = first_value + second_value
    return f_sum(sum_values)

print(sum_two_values_and_add_one(5, 2, sum_one))
print(sum_two_values_and_add_one(5, 2, sum_five))

### Clousures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_clousure = sum_ten(1)
print(add_clousure(5))
print(sum_ten(5)(1))

### Built-in higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter

def filter_greater_that_ten(number):
    return number > 10

print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values,numbers))