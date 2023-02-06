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
