#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:20:21 2023

@author: Exactas_Programa
"""
import random

def tirar_cubilete():
    
    lista_dados = []
    contador_dados = 0
    
    while contador_dados < 5:
        lista_dados.append(random.randint(0,6))
        contador_dados +=1
    
    return lista_dados


def cuantos_hay(elemento, lista):
    
    index_contador = 0
    contador2 = 0 
    
    while index_contador < len(lista):
        if lista[index_contador] == elemento:
            contador2 += 1
            
        index_contador += 1
         
    return contador2
    
#print(cuantos_hay(1,tirar_cubilete()))
 
def puntos_por_uno(lista_dados):
    
    cantidad_unos = cuantos_hay(1, lista_dados)
    
    puntaje_unos = cantidad_unos * 100
    
    if cantidad_unos == 5:
        return 10000
    elif cantidad_unos == 4:
        return 1100
    elif cantidad_unos == 3:
        return 1000
    else:
        return puntaje_unos

def puntos_por_cinco(lista_dados):
    
    cantidad_cincos = cuantos_hay(5, lista_dados)
    
    puntaje_cincos  = cantidad_cincos * 50
    
    if cantidad_cincos == 5:
        return 600
    elif cantidad_cincos == 4:
        return 550
    elif cantidad_cincos == 3:
        return 500
    else: 
        return puntaje_cincos


def total_puntos(lista_dados):
    
    puntaje_total = puntos_por_uno(lista_dados) + puntos_por_cinco(lista_dados)
    
    return puntaje_total


#print(total_puntos(tirar_cubilete()))    

def jugar_ronda(k):
    
    turno = 0
    numero_jugador = k
    lista_puntajes = []
    
    while turno < numero_jugador:
        
        lista_puntajes.append(total_puntos(tirar_cubilete()))
        
        turno +=1
        
    return lista_puntajes

#print(jugar_ronda(5))

def acumular_puntajes(puntajes_acumulados, puntajes_ronda):
    
    for i in range(len(puntajes_acumulados)):
        puntajes_acumulados[i] = puntajes_acumulados[i] + puntajes_ronda[i]
        
    return puntajes_acumulados

"""
lista1 = tirar_cubilete()
lista2 = jugar_ronda(5)

print(lista1)
print(lista2)
print(acumular_puntajes(lista1, lista2))
"""

def hay_10k(puntajes):
    
    hay_ganador = False
    
    for i in range(len(puntajes)):
        if puntajes[i] >= 10000:
            hay_ganador = True
            
    return hay_ganador


def partida_completa(k):
    
    cantidad_rondas = 0
    acumulador = jugar_ronda(k)
     
    hay_ganador = hay_10k(acumulador)
    
    while not hay_ganador:     
        acumulador = acumular_puntajes(acumulador, jugar_ronda(k))
        
        hay_ganador = hay_10k(acumulador)
        cantidad_rondas += 1
    return cantidad_rondas

def experimento(num_experiencias, k):

    cant_rondas = []
    for i in range(num_experiencias):
        cant_rondas.append(partida_completa(k))
    promedio_rondas = sum(cant_rondas) / len(cant_rondas)
    print(promedio_rondas)    
    return promedio_rondas


jugadores = 10
registro_casos_favorables = 0
repeticiones_experimento = 100
contador = 0
turnos_max = 18
while contador < repeticiones_experimento:
    promedio_rondas = experimento(repeticiones_experimento,jugadores)
    if promedio_rondas <= turnos_max:
        registro_casos_favorables += 1
    contador +=1

chance = registro_casos_favorables / repeticiones_experimento

print(chance)
