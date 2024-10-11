# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión.
# La fórmula la he buscado en google, y no estoy seguro si coincide con lo que se nos pide.
cantidad_a_invertir = float(input("Cantidad a invertir: "))
interes_anual = float(input("Interés anual (%): "))
numero_de_años = int(input("Número de años: "))
capital_obtenido = cantidad_a_invertir * ((1 + (interes_anual / 100)) ** numero_de_años)
print(f"El capital obtenido en la inversión es: {capital_obtenido:.2f}")