### Error Types ###

# SyntaxError
# print "¡Hola comunidad!" # Error
print("¡Hola comunidad!")

# NameError
# print(language) # Error
language = "Spanish"
print(language)

# IndexError
my_list= ["Python", "Swift", "kotlin", "Dart", "Javascript" ]
# print(my_list[5]) # Error
print(my_list[0])
print(my_list[4])
print(my_list[-1])

# ModuleNotFoundError
# import maths # Error
import math

# AtrributeError
#print(math.PI) # Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Carlos Javier", "Apellido": "Lozano", "Edad": 36, 1: "Python"}
#print(my_dict["Apelido"]) # Error
print(my_dict["Apellido"])

# TypeError
# print(my_list["0"]) # Error
print(my_list[0])

# ImportError
