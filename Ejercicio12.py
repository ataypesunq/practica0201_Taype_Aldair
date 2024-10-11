# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca 
# y la ganancia final total.
precio_barras_pan = 3.49
descuento_no_día = 0.60
barras_vendidas_dia = int(input("Barras vendidas del día: "))
barras_vendidas_no_dia = int(input("Barras vendidas que no son del dia: "))
Ganancia = (barras_vendidas_dia * precio_barras_pan) + (barras_vendidas_no_dia * (precio_barras_pan * descuento_no_día))
print(f"La ganancia final total es: {Ganancia}")
