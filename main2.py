# Reto 3 - Nivel 2
try: 
    n_alumnos = int(input("¿Cuántos alumnos evaluarás? "))
    n_notas = int(input("¿Cuántas notas quieres ingresar por alumno? "))
    alumnos=[]
    notas=[] 
    for x in range(n_alumnos):
        print(f'Ingresa el nombre del alumno {x+1}')
        alumno = input('Nombre: ')
        alumnos.append(alumno)
        print (f"De acuerdo, ahora ingresa las notas de {alumnos[x]}.")
        for a in range(n_notas):
            while True:
             print(f'Ingrese la nota {a+1}')
             nota = int(input('Nota: ')) #int(input("..."))
             if nota >= 0 and nota <=20:
                print (f'Nota {a+1} correctamente ingresada')
                notas.append(nota)
                break
             else:
                print ('Nota incorrecta. Ingresa una nota entre 0 y 20')      
        notas.sort()
        print(f'La mayor nota de {alumnos[x]} es: {notas[-1]}')
        print(f'La menor nota de {alumnos[x]} es: {notas[0]}')
        print(f'La nota promedio de {alumnos[x]} es: {sum(notas)/len(notas)}')
        print('***************************')
except Exception as e:
    print (e)
    print("Debes registrar un número entero")
