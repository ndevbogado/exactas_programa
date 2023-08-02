#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:05:33 2023

@author: Exactas_Programa
"""

import random

def llenar_album(longitud_album):
    album = [0]*longitud_album
    contador = 0
    
    while sum(album) < longitud_album:
        figu = random.randint(0,longitud_album - 1)
        contador = contador + 1
        album.append(figu)
        
    return contador
    