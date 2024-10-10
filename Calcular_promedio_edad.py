 
# Calcular el promedio de 22 edades
# Calcular el promedio de 22 notas
# Calcular el promedio de 22 mesadas 

def validar_edades():
    edad = # Inicialmente fuera del rango deseado 
    while ((edad < 10 ) or (edad > 20 )):
        try:
            edad = int (input("ingrtese edad del alumno: "))
            if edad < 10:
                print("La edad es muy pequeña, debe ser mayor o igual a 10... Inténtelo de nuevo.")
                if edad > 20:
                    print("La edad es muy grande0, debe ser menor o igual a 20... Inténtelo de nuevo.")
        except ValueError:
          print("Debe escribir la edad como un número entero")
        print("")
    return edad 

def validar_nota():
    nota = 0 # Inicialmente fuera del rango deseado 
    while((nota < 1) or (nota > 7)):
        try:
            nota = float (input("Ingrese nota del almuno: "))  
            if nota < 1:
                    print("Nota muy pequeña, debe ser mayor o igual que 1,0... Inténtelo de nuevo.") 
            if nota > 7:
                    print("Nota muy grande, debe ser menor o igual qie 7.0...Intélo de nuevo.")
        except ValueError:
             print("Debe escribir la nota como número decimal") 
        print("") 
    return nota

def validar_especialidad ():
     especialidades_validas = ["Introduce tu especialidad (programación, administración, contabilidad"]

     while True:
          especialidad = input("Introduce tu especialidad (programación, administración, contabilidad)").lower()  

          if especialidad in especialidades_validas:
               print(f"Especialidad '{especialidad}' valido correctamente.")
               print("")
               return especialidad
          else:
               print("Opción no válida. Por favor, intenta de nuevo.")
def promedio (a,b,c):
     prom = (a + b + c)/3
     return prom


print ("Bienvenido Septiembre...TIKI TIKI TIIIII") 
print ("")

# Inicializacion de los arreglos ARRAY o listas

nombre = [0,0,0]
especialidad = [0,0,0]
edad = [0,0,0]
mesada = [0,0,0]
