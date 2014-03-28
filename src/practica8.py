#!/usr/bin/python
#!encoding: UTF-8
import moduloerror
import sys
if((len(sys.argv)==1) or (leng(sys.argv)==2)):
  print ("No se han introducido los valores necesarios. Se utilizarán los valores predeterminados")
  print("Intervalos= 10  Veces=10  umbral 0.1")
  k=10
  n=10
  umbral=0.1
else:
  n= int(sys.argv[2])
  k= int(sys.argv[1])
  umbral=int(sys.argv[3])
print error (n, k, umbral)