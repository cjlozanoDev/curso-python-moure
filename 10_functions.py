### Functions ###

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

def sum_two_values(first_value,  second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(545345, 724234)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_value,  second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)