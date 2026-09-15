print("=== CALCULO DE NOTAS ===")

nombre = input("Nombre del estudiante: ")

nota1 = float(input("Digite la primera nota: "))
nota2 = float(input("Digite la segunda nota: "))
nota3 = float(input("Digite la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3
nota_mayor = max(nota1, nota2, nota3)
nota_menor = min(nota1, nota2, nota3)

print("\n=== RESULTADOS ===")
print("Estudiante:", nombre)
print("Promedio:", round(promedio, 2))
print("Nota mayor:", nota_mayor)
print("Nota menor:", nota_menor)

if promedio >= 3:
    print("Resultado final: APROBADO")
else:
    print("Resultado final: NO APROBADO")
