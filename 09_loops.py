### Loops ###

# While

my_condition = 0

while my_condition < 10: 
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
        break
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (36, 1.77, "Carlos Javier", "Lozano", "Carlos Javier")

for element in my_tuple:
    print(element)

my_set = {"Carlos Javier", "Lozano", 36}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Carlos Javier", "Apellido": "Lozano", "Edad": 36, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")


for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")

