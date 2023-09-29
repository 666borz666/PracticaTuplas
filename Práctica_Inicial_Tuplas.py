#Elaborado por: Daniel Campos y Junior Monge
#Fecha de Creación: 29/09/2023 8:55am
#Ultima Modificación: 29/09/2023
#Versión: 3.10.6
#importación de librerias

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

#reto 5

#programa principal
#reto 2
"""
tupla1=("calor","ayer","el","mañana")
tupla2=("ayer hizo bastante calor","en el laboratorio hace calor")
contarPalabras(tupla1,tupla2)
"""
#reto 3
esParAmigable((220, 284))  
#esParAmigable ((15, 18))  
#esParAmigable ((1210, 1184))  
#esParAmigable ((890, 890))  
#reto 4

#reto 5
