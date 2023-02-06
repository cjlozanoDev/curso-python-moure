### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Carlos Javier", "Lozano", 36}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("cjLozanoDev") # Un set no es una estructura ordenada
print(my_other_set)

my_other_set.add("cjLozanoDev") # Un set no admite repetidos
print(my_other_set)

print("cjLozanoDev" in my_other_set)
print("cjLozaniDev" in my_other_set)

my_other_set.remove("Lozano")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Carlos Javier", "Lozano", 36}
my_list = list(my_set) # Transformación arriesgada ya que no conocemos el orden de los elementos al crearse el set 
print(my_list)
print(my_list[0])

my_other_set = {"Vue", "JavaScript", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Node", "MongoDB"}))

print(my_new_set.difference(my_set))