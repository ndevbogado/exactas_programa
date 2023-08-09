import random

import numpy as np

import matplotlib.pyplot as plt

def ingresar_coord():
    x = int(input("Ingresar coord 'X': "))
    y = int(input("Ingresar coord 'Y': "))
    return (x,y)

def crear_tablero(n,m):
    n = int(n) + 2
    m = int(m) + 2
    tablero = np.repeat(" ", n*m).reshape(n,m)
    
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:
                tablero[(i,j)] = "M"
    return tablero

def es_borde(tablero, coord):
    return tablero[coord] == "M"

def vecino(tablero, coord):
    lista_vecinos = []
    x = coord[0]
    y = coord[1]

    coord_vecinos = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)]
    
    for i in coord_vecinos:
        if not es_borde(tablero, i):
            lista_vecinos.append(tablero[i])
    """
    x = coord[0]
    y = coord[1]
    for i in range(x-2,x+1):
        for j in range(y-2,y+1): 
            lista_vecinos.append(tablero[(i+x,j+y)])
    """
    return lista_vecinos

n = input("Ingresar primer valor entero: ")
m = input("Ingresar segundo valor entero: ")

tablero = crear_tablero(n,m)
print(tablero)
print(vecino(tablero,ingresar_coord()))
