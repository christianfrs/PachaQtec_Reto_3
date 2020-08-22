# Reto 3 - Nivel 1
try: 
    nombre = input("¿Cómo se llama el alumno? ")
    numero = int(input("¿Cuántas notas quieres ingresar? "))
    print (f"De acuerdo, ahora ingresa las notas de {nombre}.")
    notas=[]   
    for a in range(numero):
        while True:
            print(f'Ingresa la nota {a+1}')
            nota = int(input('Nota: ')) #int(input("..."))
            if nota >= 0 and nota <=20:
                print (f'Nota {a+1} correctamente ingresada')
                notas.append(nota)
                break
            else:
                print ('Nota incorrecta. Ingresa una nota entre 0 y 20')      
    notas.sort()
    print(f'La mayor nota de {nombre} es: {notas[-1]}')
    print(f'La menor nota de {nombre} es: {notas[0]}')
    print(f'La nota promedio de {nombre} es: {sum(notas)/len(notas)}')
except Exception as e:
    print (e)
    print("Debes registrar un número entero")
