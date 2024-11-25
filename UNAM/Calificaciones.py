import random

# Función para calcular el promedio
def calcular_promedio(materias):
    total_calificaciones = 0
    total_creditos = 0
    for materia in materias:
        calificacion = materia['calificacion']
        creditos = materia['creditos']
        
        # Si la calificación es NP (No Presentado), cuenta como 0
        if calificacion == 'NP':
            calificacion = 0
        else:
            calificacion = float(calificacion)
        
        total_calificaciones += calificacion * creditos
        total_creditos += creditos
    
    if total_creditos == 0:
        return 0  # Evitar división por cero
    promedio = total_calificaciones / total_creditos
    return promedio

# Lista completa de materias con calificaciones conocidas y NP para materias pendientes
materias = [
    # Primer semestre
    {'nombre': 'Matemáticas I', 'calificacion': 5, 'creditos': 10},
    {'nombre': 'Taller de Cómputo', 'calificacion': 6, 'creditos': 8},
    {'nombre': 'Química I', 'calificacion': 6, 'creditos': 8},
    {'nombre': 'Historia Universal Moderna y Contemporánea I', 'calificacion': 'NP', 'creditos': 8},
    {'nombre': 'Taller de Lectura y Redacción I', 'calificacion': 6, 'creditos': 12},
    {'nombre': 'Inglés I', 'calificacion': 6, 'creditos': 8},

    # Segundo semestre
    {'nombre': 'Matemáticas II', 'calificacion': 5, 'creditos': 10},
    {'nombre': 'Química II', 'calificacion': 5, 'creditos': 8},
    {'nombre': 'Historia Universal Moderna y Contemporánea II', 'calificacion': 'NP', 'creditos': 8},
    {'nombre': 'Taller de Lectura y Redacción II', 'calificacion': 5, 'creditos': 12},
    {'nombre': 'Inglés II', 'calificacion': 5, 'creditos': 8},

    # Tercer semestre
    {'nombre': 'Matemáticas III', 'calificacion': 'NP', 'creditos': 10},
    {'nombre': 'Física I', 'calificacion': 5, 'creditos': 10},
    {'nombre': 'Biología I', 'calificacion': 5, 'creditos': 10},
    {'nombre': 'Historia de México I', 'calificacion': 'NP', 'creditos': 8},
    {'nombre': 'Taller de Lectura y Redacción III', 'calificacion': 'NP', 'creditos': 12},
    {'nombre': 'Inglés III', 'calificacion': 'NP', 'creditos': 8},

    # Cuarto semestre
    {'nombre': 'Matemáticas IV', 'calificacion': 'NP', 'creditos': 10},
    {'nombre': 'Física II', 'calificacion': 6, 'creditos': 10},
    {'nombre': 'Biología II', 'calificacion': 'NP', 'creditos': 10},
    {'nombre': 'Historia de México II', 'calificacion': 'NP', 'creditos': 8},
    {'nombre': 'Taller de Lectura y Redacción IV', 'calificacion': 'NP', 'creditos': 12},
    {'nombre': 'Inglés IV', 'calificacion': 'NP', 'creditos': 8},

    # Quinto semestre
    {'nombre': 'Administración', 'calificacion': 'NP', 'creditos': 10},
    {'nombre': 'Filosofía', 'calificacion': 9, 'creditos': 10},
    {'nombre': 'Física III', 'calificacion': 8.5, 'creditos': 10},
    {'nombre': 'Cálculo Diferencial e Integral', 'calificacion': 9, 'creditos': 10},
    {'nombre': 'Psicología I', 'calificacion': 8.5, 'creditos': 10},
    {'nombre': 'Latín I', 'calificacion': 8.5, 'creditos': 10},
    {'nombre': 'Cibernética', 'calificacion': 9, 'creditos': 10},
]

# Promedio inicial
promedio_inicial = 5.20

# Número de simulaciones
num_simulaciones = 10000
promedio_objetivo = 8.0  # Cambia a 7.0, 8.0 o 9.0 según el promedio objetivo
exito = False
mejor_promedio = 0  # Para almacenar el mejor promedio encontrado

for i in range(num_simulaciones):
    # Crear una copia de las materias para modificar las NP y calificaciones de 5 sin afectar el original
    materias_simulacion = []
    for materia in materias:
        if materia['calificacion'] == 'NP' or materia['calificacion'] == 5:
            # Asignar una calificación aleatoria entre 7 y 10 a las materias recuperables
            calificacion_aleatoria = random.randint(7, 9)
            materias_simulacion.append({'nombre': materia['nombre'], 'calificacion': calificacion_aleatoria, 'creditos': materia['creditos']})
        else:
            # Mantener la calificación existente para materias ya calificadas y no mejorables
            materias_simulacion.append(materia)
    
    # Calcular el promedio para esta simulación
    promedio = calcular_promedio(materias_simulacion)
    
    # Actualizar el mejor promedio si este es superior
    if promedio > mejor_promedio:
        mejor_promedio = promedio
    
    # Verificar si el promedio alcanza o supera el objetivo
    if promedio >= promedio_objetivo:
        exito = True
        print(f'Simulación {i + 1}: Lograste un promedio de {promedio:.2f} con las siguientes calificaciones:')
        for materia in materias_simulacion:
            print(f"  - {materia['nombre']}: {materia['calificacion']}")
        break  # Salir si encontramos una simulación exitosa
    else:
        print(f'Simulación {i + 1}: No se alcanzó el promedio objetivo. Promedio obtenido: {promedio:.2f}')

# Si no se alcanzó el promedio objetivo en ninguna simulación
if not exito:
    print(f"\nNo se logró alcanzar un promedio de {promedio_objetivo} en {num_simulaciones} simulaciones.")
    print(f"El mejor promedio alcanzado fue: {mejor_promedio:.2f}")
