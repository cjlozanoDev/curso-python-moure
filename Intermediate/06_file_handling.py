### File handling ###

import os, json

# .txt files

txt_file = open("Intermediate/my_file.txt", "w+")
txt_file.write("Mi nombre es Carlos Javier\nMi apellido es Lozano\nMi edad son 36 años\nMi lenguaje favorito es Python")
# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())
# print(txt_file.readline())
# print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\naunque también me gusta javascript")
txt_file.close()

# os.remove("Intermediate/my_file.txt")

# .json file

json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name": "Carlos Javier",
    "surname": "Lozano",
    "age": 36,
    "languages": ["Python", "Javascript", "Swift"],
    "website": "https://github.com/cjlozanodev"}

json.dump(json_test, json_file, indent = 2)

