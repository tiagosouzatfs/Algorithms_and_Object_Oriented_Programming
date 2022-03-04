#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 10:07:05 2019

@author: tiago
"""

from random import randint

print()

n = int(input('Como é uma matriz quadrada, digite a dimensão: '))

mat = [0]*n

for i in range(n):
    mat[i] = [0]*n

print("A Matriz original:")

for i in range(n):
    for j in range(n):
        mat[i][j] = randint(1,9) #input('Digite um valor: ')
             
print()

for i in range(n):
    for j in range(n):
        print('[' + str(mat[i][j]) + ']', end='')
    print()

print()

print("A nova matriz:")

print()

tronop = 0
tronos = 0
aux = n
d = -1
for i in range(n):
    aux-=1
    d+=1
    for j in range(n):
        if i==j:
            tronop = mat[i][j]
            mat[i][j] = mat[i][aux]
            mat[i][aux]=tronop
            
        if i>j:
            tronos = mat[i][j]
            mat[i][j] = mat[i][d]
            mat[i][d]=tronos
            
        print('[' + str(mat[i][j]) + ']', end='')
    print()

        