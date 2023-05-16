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

json_file.close()

with open("Intermediate/my_file.json") as my_other_json_file:
    for line in my_other_json_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "Surname", "Age", "language", "Website"])
csv_writer.writerow(["Carlos Javier", "Lozano", 36, "python", "https://github.com/cjlozanodev"])
csv_writer.writerow(["Roswel", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_csv_file:
    for line in my_other_csv_file.readlines():
        print(line)


