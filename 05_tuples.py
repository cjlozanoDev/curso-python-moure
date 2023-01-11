### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

print(type(my_tuple))
print(type(my_other_tuple))

my_tuple = (36, 1.77, "Carlos Javier", "Lozano", "Carlos Javier")
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Carlos Javier"))
print(my_tuple.index("Lozano"))
print(my_tuple.index("Carlos Javier"))

my_tuple[1] = 1.80
print(my_tuple)