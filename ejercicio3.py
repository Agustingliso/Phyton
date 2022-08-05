from ctypes.wintypes import INT


print ("ingrese numero de respuestas correctas: ")
RC= int (input())
print ("Ingrese Numero de respuestas incorrectas: ")
RI= int (input())
print ("ingrese numero de respuestas en blanco: ")
RB= int (input())


PRC= RC*3
PRI= RI*-1
PRB= RB*0

PF= PRC+PRI+PRB
print ("El puntaje total es:", PF)