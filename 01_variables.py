# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_str_variable = str(my_int_variable)
print(my_int_str_variable)
print(type(my_int_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_str_variable, my_string_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Carlos Javier", "Lozano", "cjlozano", 35
print("Me llamo:", name, surname, ". Mi edad es:", age, "y mi alias es:", alias)

print(my_string_variable, my_int_str_variable, my_string_variable)

name = input('Cuál es tu nombre?')
edad = input('¿Cuántos años tienes?')

print(name)
print(edad)