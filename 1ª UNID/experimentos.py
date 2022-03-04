#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 10:07:05 2019

@author: tiago
"""

nota = [[7, 10], [5, 6]]

print("-----------")
for i in range(len(nota)): 
  for j in range(len(nota[i])): 
      print("["+ str(nota[i][j])+"]", end = '')
  print()
print("-----------") 

for i in range(len(nota)): 
  for j in range(len(nota[i])):
      print("["+ str(nota[i][j])+"]")
  print()
print("-----------")  
