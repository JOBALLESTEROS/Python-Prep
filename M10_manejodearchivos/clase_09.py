import sys

if len(sys.argv)==4:
    print('El parametro 1 es: ', sys.argv[1])
    print('El paramatro 2 es:', sys.argv[2])
    print('El parametro 3 es: ', sys.argv[3])
else:
    print('La cantidad de parametros no debe ser diferente de (3)')