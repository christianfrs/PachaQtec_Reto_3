# Reto 3 - Nivel 2
try: 
    n_alumnos = int(input("¿Cuántos alumnos evaluarás? "))
    n_notas = int(input("¿Cuántas notas quieres ingresar por alumno? "))
    alumnos=[]
    notas=[] 
    may_notas=[]
    men_notas=[]
    prom_notas=[]
    resumen=[]
    headers=[]
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
        may_notas.append(notas[-1])
        men_notas.append(notas[0])
        prom_notas.append(sum(notas)/len(notas))
        print(f'La mayor nota de {alumnos[x]} es: {notas[-1]}')
        print(f'La menor nota de {alumnos[x]} es: {notas[0]}')
        print(f'La nota promedio de {alumnos[x]} es: {sum(notas)/len(notas)}')
        print('***************************')
        notas.clear()
    resumen = zip (alumnos,may_notas,men_notas,prom_notas)
    from tabulate import tabulate
    print(tabulate(tuple(resumen),headers=['Alumno','Nota max','Nota min','Nota prom']))

except Exception as e:
    print (e)
    print("Debes registrar un número entero")
