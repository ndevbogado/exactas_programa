#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:48:58 2023

@author: Exactas_Programa
"""
import random 

def cuantas_figus(figus_total):
    album = [0] * figus_total
    figus_adquiridas = 0
    
    while sum(album) < figus_total:
        figu = random.randint(0, figus_total - 1)
        album[figu] = 1
        figus_adquiridas = figus_adquiridas + 1
    

    return figus_adquiridas


def repetir_proceso(figus_total, n_rep):
    resultados = []
    contador = 0
    while contador < n_rep:
        
        resultados.append(cuantas_figus(figus_total))
        
        contador = contador + 1
        
    return resultados

def promedio_cuantas_figus(figus_total, n_rep):
    
    resultados = repetir_proceso(figus_total, n_rep)

    promedio = sum(resultados)/len(resultados)
    
    return promedio

def cantidad_figus_esperada(figus_total):
    
    lista = [] 
    repetidor = 0
    while repetidor < figus_total:
        termino = figus_total/(figus_total - repetidor)
        lista.append(termino)
        repetidor = repetidor + 1
        
    cantidad_esperada = sum(lista)
    return cantidad_esperada

def dame_chances(resultados, cantidad_maxima):
    contador = 0
    cant_casos_favorables = 0
    
    while contador < len(resultados):
        valor = resultados[contador]
        
        if valor <= cantidad_maxima:
            cant_casos_favorables = cant_casos_favorables + 1
        contador = contador +1
    
    chances = cant_casos_favorables / cantidad_maxima
    
    return chances


def simular_chances(figus_total, cantidad_max, n_rep):
    
    resultados = repetir_proceso(figus_total, n_rep)
    
    chances = dame_chances(resultados, cantidad_max)
    
    return chances
        
        
        
    

print(promedio_cuantas_figus(6,1000))
print(promedio_cuantas_figus(12,1000))
print(cantidad_figus_esperada(12))
print(dame_chances([12,23,14,11,7,19,11,29,10,8],11))
print(simular_chances(6,11,100))