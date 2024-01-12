class funciones():
    def __init__(self, lista_num):
        self.lista= lista_num 
        
    def verifica_primo(self):
        for i in self.lista:
            if (self.__verifica_primo(i)):
               print('el elemento',i, ' es un número primo')
            else:
               print('el elemento',i,'no es primo')
            
    def grados(self,origen, destino):
        for i in self.lista:
            print(i,'grados','son',origen,self.__grados(i,origen,destino),'grados',destino)
            
    def factorial(self):
        for i in self.lista:
            print('el factortial de ',i,'es',self.__factorial(i))
        
    
    def __verifica_primo(self, numero):
        es_primo=True
        for i in range(2,numero):
            if numero%i ==0:
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
        while numero <=0:
            print(' No se puede operar con el número ingresado')
            break
        if numero>1:
             numero=numero*self.factorial(numero-1)
        return numero
        