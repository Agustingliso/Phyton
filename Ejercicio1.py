from asyncore import read
from re import T
from time import time
from turtle import distance


print ("Ingrese la velocidad y el tiempo de la unidad movil")

V = float( input("Velocidad: "))
T= int(input("tiempo: "))
D= V * T
print (D)
