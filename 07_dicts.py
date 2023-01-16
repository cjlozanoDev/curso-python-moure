### Dictionaries #### 

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Carlos Javier", "Apellido": "Lozano", "Edad": 36, 1: "Python"}

my_dict = {
  "Nombre": "Carlos Javier",
  "Apellido": "Lozano",
  "Edad": 36,
  "Lenguajes": {"Python", "JavaScritp", "Vue"},
  1: 1.73,
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"]  = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle carlosj"
print(my_dict)

del my_dict["Calle"]
print(my_dict)