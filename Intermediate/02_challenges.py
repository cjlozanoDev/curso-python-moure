### Challenges ###

"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """

def isFizz(number):
    return number % 3 == 0

def isBuzz(number):
    return number % 5 == 0

def isFizzbuzz(number):
    return number % (3 * 5) == 0

def fizzbuzz():
    for index in range(100):
        number = index + 1
        if isFizzbuzz(number):
            print("fizzBuzz")
        elif isFizz(number):
            print("fizz")
        elif isBuzz(number):
            print("buzz")
        else: 
            print(number)

fizzbuzz()


"""
¿ES UN ANAGRAMA?

Escribe una función que reciba dos palabras (String) y retorne
  * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(word_one, word_two):
    if (len(word_one) != len(word_two)):
        return False
    for letter in word_one:
        if word_one.lower().count(letter) != word_two.lower().count(letter):
            return False
    return True    

is_words_anagrams = is_anagram("delira", "lidera")
print(is_words_anagrams)


"""
 SUCESIÓN DE FIBONACCI

 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci_sucession():
    before_number = 0;
    current_number = 1;
    for i in range(0, 50):
      print(before_number)
      next_number = current_number + before_number
      before_number = current_number;
      current_number = next_number;

fibonacci_sucession()


"""
 ¿ES UN NÚMERO PRIMO?

 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime(number):
    if number < 2:
        return False

    number_before = number - 1;
    while number_before > 1:
        if number % number_before == 0:
            return False
        number_before -= 1
     
    return True

for i in range(1, 101):
    if is_prime(i):
        print(i)


"""
 INVIRTIENDO CADENAS
 
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def inverter_string(text):
    length_text = len(text)
    reverse_text = ''

    for indexLetter in range(1, length_text + 1):
        reverse_text += text[length_text - indexLetter]
    
    return reverse_text

print(inverter_string("Hola mundo"))