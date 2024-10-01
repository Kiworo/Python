
def promedio_curso(promedios):
    return sum(promedios) / len(promedios)


def validar_nota():
    while True:
        try:
            nota = float(input("Ingrese la nota (1-7): "))  # Solicitar entrada del usuario
            if 1 <= nota <= 7:  # Verificar si la nota está en el rango correcto
                return nota  # Retornar la nota válida
            else:
                print("La nota debe estar entre 1 y 7. Intente nuevamente.")  # Mensaje de error
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")  # Manejo de errores para entradas no numéricas



def promedio_notas(n1, n2, n3):
    # Nota 1 vale 20%, Nota 2 vale 30%, Nota 3 vale 50%
    return (n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5)

# Inicialización de listas
alumnos = []
promedios = []
mejor_nota = []

# Ingresar datos de 5 alumnos
for i in range(5):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    apellido = input(f"Ingrese el apellido del alumno {i + 1}: ")
   
    # Ingresar las notas
    print(f"alumno:  {nombre} {apellido}")
    print("PRIMERA NOTA")
    nota1 = validar_nota()
    print("")
    print("SEGUNDA NOTA")
    nota2 = validar_nota()
    print("")
    print("TERCERA NOTA")
    nota3 = validar_nota()

    nota1 = float(input(f"Ingrese la nota 1 del alumno {nombre} {apellido}: "))
    nota2 = float(input(f"Ingrese la nota 2 del alumno {nombre} {apellido}: "))
    nota3 = float(input(f"Ingrese la nota 3 del alumno {nombre} {apellido}: "))
   # Llamar a la función
    nota_valida = validar_nota()
    print(f"Nota válida ingresada: {nota_valida}")

    # Calcular el promedio del alumno
    promedio = promedio_notas(nota1, nota2, nota3)
    alumnos.append((nombre, apellido, nota1, nota2, nota3, promedio))
    promedios.append(promedio)
    mejor_nota.append(max(nota1, nota2, nota3))

# Calcular el promedio total del curso
promedio_total_curso = promedio_curso(promedios)

# Calcular la mejor nota entre los promedios
mejor_promedio = max(promedios)

# Mostrar resultados
print("\nResultados:")
for alumno in alumnos:
    print(f"Alumno: {alumno[0]} {alumno[1]}, Promedio: {alumno[5]:.2f}, Mejor Nota: {max(alumno[2], alumno[3], alumno[4]):.2f}")

print(f"\nPromedio total del curso: {promedio_total_curso:.2f}")
print(f"Mejor promedio en el curso: {mejor_promedio:.2f}")

