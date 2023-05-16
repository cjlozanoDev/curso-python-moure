### Regular Expressions ###

import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])


match = re.match("Esta no es la lección", my_other_string)

if match != None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])



print(re.match("Expresiones regulares", my_string))

# search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)

# split 

print(re.split(":", my_string))

# Sub

re.sub()
