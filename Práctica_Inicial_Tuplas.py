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

#reto 4

#reto 5
