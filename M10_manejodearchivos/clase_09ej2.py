import sys

if len (sys.argv)==2:
    import datetime
    import os
    tiempo= datetime.datetime.now()
    tiempo= int(datetime.datetime.timestamp(tiempo))
    
    lluvia=sys.argv[1]
    temperatura= input('Ingrese la temperatura en grados centigrados')
    humedad = ('ingrese el % de humedad')
    resultado= str(tiempo)+','+temperatura+','+humedad+','+lluvia
    
    logs_lluvia = open('clase_09ej2.csv', 'a')
    logs_lluvia.write(resultado+'\n')
    logs_lluvia.close()
    
else:
    print('La cantidad de valores ingresados no debe ser diferente de (3)')
