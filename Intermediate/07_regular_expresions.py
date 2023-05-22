### Regular Expressions ###

import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
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

print(re.sub("lección|Lección", "LECCIÓN", my_string))
# haría lo mismo que la anterior print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Patterns

pattern = r"[l|L]ección"
print(re.findall(pattern, my_string))

pattern = r"[l|L]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "carlosjlp@gmail.com"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
print(re.match(pattern, email))

