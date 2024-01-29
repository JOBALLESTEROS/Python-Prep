class funciones():
    def __init__(self, lista_numeros):
        if (type(lista_numeros) != list):
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de números enteros')  
        else:
            self.lista = lista_numeros
        
    def verifica_primo(self):
        lista_primo=[]
        for i in self.lista:
            if (self.__verifica_primo(i)):
               lista_primo.append(True)
            else:
               lista_primo.append(False)
        return lista_primo
            
    def grados(self,origen, destino):
        parametro=['Celcius','Farenheit','Kelvin']
        lista_conversión=[]
        if str(origen) not in parametro:
            print('Los parametros esperados deben ser ',parametro)
            return lista_conversión
        if str(destino) not in parametro:
            print('Los parametros esperados deben ser ',parametro)
            return lista_conversión
        for i in self.lista:
            lista_conversión.append(self.__grados(i,origen,destino))
            return lista_conversión
            
    def factorial(self):
        lista_factorial=[]
        for i in self.lista:
            lista_factorial.append(self.__factorial(i))
            return lista_factorial
    
    def __verifica_primo(self, numero):
        es_primo=True
        for i in range(2,numero):
            if numero % i ==0:
              es_primo=False
            break   
        return es_primo
    
    def valor_repetido(self,bajo):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if(bajo):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
               i = lista_unicos.index(elemento)
               lista_repeticiones[i] += 1
            else:
               lista_unicos.append(elemento)
               lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
               moda = lista_unicos[i]
               maximo = lista_repeticiones[i]
        return moda, maximo
    
    def __grados (self,numero,tipo1,tipo2):
        valor= None
        if tipo1 == 'Celcius':
           if tipo2== 'Celcius':
            valor=numero
           elif tipo2=='Farenheit':
            valor =(numero*9/5)+32
           elif tipo2=='Kelvin':
            valor=numero+273.5
           else:
               ('No se reconoce el valor tipo2')
        elif tipo1 == 'Farenheit':
            if tipo2== 'Celcius':
               valor=(numero-32)*5/9
            elif tipo2=='Farenheit':
               valor =numero
            elif tipo2=='Kelvin':
              valor=((numero-32)*5/9)+273.5
            else:
               ('No se reconoce el valor tipo2')
        elif tipo1 == 'Kelvin':
            if tipo2== 'Celcius':
              valor=numero-273.5
            elif tipo2=='Farenheit':
              valor =((numero-273.5)*9/5)+32
            elif tipo2=='Kelvin':
              valor=numero
            else:
               ('No se reconoce el valor tipo2')
        else:
            ('No se reconoce el valor tipo1') 
        return  valor
    
    def __factorial(self,numero):
       if(type(numero) != int):
            return 'El numero debe ser un entero'
       if(numero < 0):
            return 'El numero debe ser pisitivo'
       if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
       return numero