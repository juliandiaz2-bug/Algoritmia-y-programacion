notas = {
"Harry": [3.8, 4.0, 4.2],
"Ron": [3.2, 3.8, 2.8],
"Hemione": [5.0, 5.0, 5.0],
"Daco": [4.5, 4.2, 5.0],
"Nevil": [2.5, 3.0, 3.2]
}
def calcular_promedio_simple(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)
def calcular_promedio_ponderado(lista):
    if len(lista) == 0:
        return 0 
    porcentajes = [0.3, 0.3, 0.4]
    sum_ponderada = 0
    for i in range(len(lista)):
        sum_ponderada += lista[i] * porcentajes[i]      
    return sum_ponderada
def estudiantes_con_promedio_mayor_a(lista, umbral):
    return [estudiante for estudiante in notas if calcular_promedio_simple(notas[estudiante]) > umbral]
def estudiantes_aprobados(lista, umbral):
    return [estudiante for estudiante in notas if calcular_promedio_ponderado(notas[estudiante]) >= umbral]
umbral_simple = 3.0
umbral_ponderado = 3.0
print("Promedio simple de cada estudiante:")
for estudiante, calificaciones in notas.items():
    print(f"{estudiante}: {calcular_promedio_simple(calificaciones):.2f}") 
print("Promedio ponderado de cada estudiante:")
for estudiante, calificaciones in notas.items(): #.items() devuelve una vista de los pares clave-valor del diccionario, lo que permite iterar sobre ambos al mismo tiempo
    print(f"{estudiante}: {calcular_promedio_ponderado(calificaciones):.2f}")
print(f"Estudiantes aprobados con promedio mayor o igual a 3.0 y promedio mayor o igual a 3.0: {[estudiante for estudiante in notas if calcular_promedio_simple(notas[estudiante]) >= 3.0 and calcular_promedio_ponderado(notas[estudiante]) >= 3.0]}")
print(f"Estudiantes desaprobados con promedio simple menor a 3.0 y promedio ponderado menor a 3.0: {[estudiante for estudiante in notas if calcular_promedio_simple(notas[estudiante]) < 3.0 and calcular_promedio_ponderado(notas[estudiante]) < 3.0]}")
