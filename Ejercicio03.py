# Escribir un programa que pregunte el nombre del usuario en la consola y después de que 
# el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, 
# donde <nombre> es el nombre que el usuario haya introducido.
# Utilizo la opción de f-string, para evitar el espacio entre el nombre y el signo de exclamación
Nombre = input("Escribe tu nombre: ")
print(f"¡Hola {Nombre}!")