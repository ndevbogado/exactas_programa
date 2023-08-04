# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import random 

def generador_bosque(n):
    bosque = []
    for i in range(n):
        bosque.append(0)
    
    return bosque

def suceso_aleatorio(n):
    probabilidad = random.randint(0,n)
    return probabilidad
    
def brotes(bosque, p):
    for i in range(len(bosque)):
        if bosque[i] == 0:
            chance = suceso_aleatorio(100)
            if chance <= p:
                bosque[i] = 1
    return bosque    

def cuantos(bosque,tipo_celda):
    contador_tipo_celda = 0
    
    for i in range(len(bosque)):
        if bosque[i] == tipo_celda:
            contador_tipo_celda += 1
    return contador_tipo_celda

def rayos(bosque, f):
    for i in range(len(bosque)):
        chance = suceso_aleatorio(100)
        if bosque[i] == 1 and (chance <= f):
            bosque[i] = -1
    return bosque
        
def propagacion(bosque):
    
    for i in range(1,len(bosque)):
        if bosque[i] == -1 and bosque[i-1]!=0:
            bosque[i-1] = -1
        if bosque[i-1] == -1 and bosque[i] !=0:
            bosque[i] = -1
          
    for i in range(len(bosque)-2,-1,-1):
        if bosque[i] == -1 and bosque[i+1]!=0:
            bosque[i+1] = -1
        if bosque[i+1] == -1 and bosque[i] !=0:
            bosque[i] = -1
            
    return bosque

def limpieza(bosque):
    for i in range(len(bosque)):
        if bosque[i] == -1:
            bosque[i] = 0
    return bosque

def dinamica(tamanio_bosque, anios, prob_brote, prob_rayo):
    bosque = generador_bosque(tamanio_bosque)
    print(f"Generador del bosque: {bosque}")
    registro_sobrevivientes = []
    for i in range(anios):
        contador_arboles = 0
        bosque = brotes(bosque, prob_brote)
        print(f"Epoca de brote: {bosque}")
        bosque = rayos(bosque, prob_rayo)
        print(f"Epoca de caida de rayos: {bosque}")
        bosque = propagacion(bosque)
        print(f"Periodo de propagacion del fuego: {bosque}")
        bosque = limpieza(bosque)
        print(f"Epoca de limpieza: {bosque}")
        cant_arboles_sup = sum(bosque)
        print(f"Arboles sobrevivientes: {cant_arboles_sup}")
        registro_sobrevivientes.append(cant_arboles_sup)
        print(f"### FINAL DEL anio {i+1} ###")
    print(f"\nregistro de sobrevivientes: {registro_sobrevivientes}")
    promedio_sobrevivientes = sum(registro_sobrevivientes) / len(registro_sobrevivientes)
    print(f"promedio: {promedio_sobrevivientes}")
    return promedio_sobrevivientes

dinamica(20,500,3,2)
"""
prop = propagacion([1, 1, 1, -1, 0, 0, 0, 1, 1, 0])
print(prop)
prop = limpieza(prop)
print(prop)
"""
    
