from random import choice, randrange
from datetime import datetime
# Operadores posibles
#1ra MODIFICACION AGREGAR LAS OPERACIONES QUE FALTAN
operators = ["+", "-","*","/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
#Inicializo nuevas variables para contar los correctos e incorrectos
correcto=0
incorrecto=0
for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
# Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
# Le pedimos al usuario el resultado
#2da MODIFICACION COMPARAR RESULTADOS E IMPRIMIR SI ES CORRECTO O INCORRECTO
#3ra MODIFICACION AGREGO CONTADOR PARA SABER LA CANTIDAD DE VECES QUE ACERTE Y LA CANTIDAD DE VECES QUE NO
    result = input("resultado: ")
    result=int(result)
    match operator:
        case "+":
            cuenta=number_1+number_2
            if(cuenta==result):
                print("Correcto")
                correcto+=1
            else:
                print("Incorrecto")
                incorrecto+=1
        case "-":
            cuenta=number_1-number_2
            if(cuenta==result):
                print("Correcto")
                correcto+=1
            else:
                print("Incorrecto")
                incorrecto+=1
        case "*":
            cuenta=number_1*number_2
            if(cuenta==result):
                print("Correcto")
                correcto+=1
            else:
                print("Incorrecto")
                incorrecto+=1
        case "/":            
            if (number_2!=0):
                cuenta=number_1/number_2
                if(cuenta==result):
                    print("Correcto")
                    correcto+=1
                else:
                    print("Incorrecto")
                    incorrecto+=1
            else:
                print("No se puede divir entre 0")        
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
#Imprimo la cantidad de correctos y incorrectos
print("La cantidad de correctos fueron: ",correcto)
print("La cantidad de incorrectos fueron: ",incorrecto)
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")