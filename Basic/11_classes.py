### Classes ###

class MyEmptyPerson:
    pass

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.__name = name # Propiedad privada
        self.__surname = surname # Propiedad privada
        self.full_name = f"{name} {surname} ({alias})" # Propiedad pública
    
    def get_name(self):
        return self.__name
    
    def walk(self):
        print(f"{self.full_name} Está caminando")
    
print(MyEmptyPerson)
print(MyEmptyPerson())

my_person = Person("Carlos Javier", "Lozano")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Carlos Javier", "Lozano", "cjlozano")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Jesus Quintero (el loco de la colina)"
print(my_other_person.full_name)

my_other_person.full_name = 888
print(my_other_person.full_name)

