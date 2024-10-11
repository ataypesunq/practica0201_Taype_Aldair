# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.
horas_trabajadas = float(input("Cuántas horas trabajadas?: "))
coste_hora = float(input("Cuál es el coste por hora?: "))
paga = horas_trabajadas * coste_hora
print(f"La paga que le corresponde es {paga:.2f} €")