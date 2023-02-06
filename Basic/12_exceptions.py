### Exceptions Handling ###

numberOne= 5
numberTwo = 1
numberTwo = "1"

# Try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")

# Try except else finaaly

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipos

try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except TypeError: # Solo capturá errores de tipo Type Error
    print("Se ha producido un TypeError")
except ValueError: # Solo capturá errores de tipo Value Error
    print("Se ha producido un ValueError")


# Captura de la información de la excepción
try:
    print(numberOne + numberTwo)
    print("No se ha producido error")
except ValueError as error: # Solo capturá errores de tipo Value Error
    print(f"Se ha producido un ValueError: {error}")
except Exception as exception:
    print(f"Se ha producido un error {exception}")