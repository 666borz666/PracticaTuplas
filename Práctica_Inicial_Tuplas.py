#Elaborado por: Daniel Campos y Junior Monge
#Fecha de Creación: 29/09/2023 8:55am
#Ultima Modificación: 29/09/2023
#Versión: 3.10.6
#importación de librerias
import sys
sys.setrecursionlimit(5000)
#creación de funciones
#reto 2
def contarPalabras(tupla1,tupla2):
    """
    """
    contarPalabras=0
    for a in tupla1:
        for b in tupla2:
            for palabras in b.split():
                if a==palabras:
                    contarPalabras+=1
        print("La palabra",a,"se repite",contarPalabras,"veces")
        contarPalabras=0
    return
#reto 3
def esParAmigable(tupla):
    """
    """
    suma1 = suma2 = 0
    for num in tupla:
        if tupla[0]!=tupla[1]:
            for i in range(1,num):
                if num == tupla[0]:
                    if num%i==0:
                        suma1+=i
                else:
                    if num%i==0:
                        suma2+=i
        else:
            return print(False)
    if suma1==tupla[1] and suma2==tupla[0]:
        return print(True)
    else:
        return print(False)
    
            
#reto 4
def mostrarCercano(tupla):
    
    dif1 = dif2 = 0
    num1 = num2 = 0
    difAux1 = difAux2 = 1000
    numFijo = tupla[0]
    for num in tupla[1:]:
        if numFijo ==num:
            return print(f"Dentro de la tupla  el número más cercano a {tupla[0]} es el mismo:", num)
        else:
            
            if num>numFijo:
               dif1 = num - numFijo
               if dif1<difAux1:
                   num1=num
                   difAux1=dif1
            elif num<numFijo:
                dif2= numFijo - num
                if difAux2>dif2:
                    num2=num
                    difAux2=dif2
    if (num1-numFijo)==abs(num2-numFijo):
         if num1<num2:
            print(num1)
         else:
            print(num2)
    else:
        if (num1-numFijo)<abs(num2-numFijo):
            print(num1)
        else:
            print(num2)
#reto 5

#programa principal
#reto 2
"""
tupla1=("calor","ayer","el","mañana")
tupla2=("ayer hizo bastante calor","en el laboratorio hace calor")
contarPalabras(tupla1,tupla2)
"""
#reto 3
##esParAmigable((220, 284))  
##esParAmigable ((15, 18))  
##esParAmigable ((1210, 1184))  
##esParAmigable ((890, 890))  
#reto 4
mostrarCercano ((8, 11, 4, 10, 100)) 
mostrarCercano ((8, 11, 10, 6, 4)) 
#reto 5
