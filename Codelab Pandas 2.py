import pandas as pd

# Crear el DataFrame desde el CSV
data = {
    'Nombre': ['Estudiante1', 'Estudiante2', 'Estudiante3', 'Estudiante4', 'Estudiante5', 'Estudiante6', 'Estudiante7', 'Estudiante8', 'Estudiante9', 'Estudiante10'],
    'Edad': [20, 21, 19, 22, 20, 21, 19, 22, 20, 21],
    'Puntuacion': [85.5, 75.0, 92.5, 80.2, 88.9, 76.8, 94.2, 82.1, 87.3, 77.6]
}

df = pd.DataFrame(data)

# Operaciones solicitadas:

# 1. Puntuación promedio de los estudiantes mayores de 20 años.
puntuacion_promedio_mayores_20 = df[df['Edad'] > 20]['Puntuacion'].mean()
print(f'Puntuación promedio de estudiantes mayores de 20 años: {puntuacion_promedio_mayores_20}')

# 2. Nombre de los estudiantes con puntuación mayor a 85 y edad menor a 22.
estudiantes_condicion = df[(df['Puntuacion'] > 85) & (df['Edad'] < 22)]['Nombre']
print(f'Estudiantes con puntuación mayor a 85 y edad menor a 22:\n{estudiantes_condicion}')

# 3. Edad y cantidad de estudiantes por cada edad. Ordenar por edad de forma descendente.
edad_cantidad_estudiantes = df['Edad'].value_counts().sort_index(ascending=False).reset_index(name='Cantidad').rename(columns={'index': 'Edad'})
print('Edad y cantidad de estudiantes por cada edad (ordenado por edad de forma descendente):\n', edad_cantidad_estudiantes)

# 4. Edad promedio de estudiantes con puntuación mayor a 80.
edad_promedio_puntuacion_80 = df[df['Puntuacion'] > 80]['Edad'].mean()
print(f'Edad promedio de estudiantes con puntuación mayor a 80: {edad_promedio_puntuacion_80}')
