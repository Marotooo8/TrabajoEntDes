# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:02:38 2021

@author: MarcosMarotoGranados
"""

opc=0
while(opc!=5):  # con este while controlamos que el programa se ejecute hasta que metamos "Salir -> 8"
    print("1.-Suma")
    print("2.-Resta")
    print("3.-Multiplicación")
    print("4.-División")
    print("5.-Salir")
    opc = int(input("Intro opc válida:"))
    while(opc<1 or opc>5):  # con este while controlamos que la opción esté en el rango correcto
        opc = int(input("Intro opc válida:"))
    

    if(opc==1): 
        x=int(input("Introduzca el primer número: "))
        y=int(input("Introduzca el segundo número: "))
        print(f"{x}+{y}={x+y}")
        
    elif(opc==2):
        x=int(input("Introduzca el primer número: "))
        y=int(input("Introduzca el segundo número: "))
        print(f"{x}-{y}={x-y}")
        
    elif(opc==3):
        x=int(input("Introduzca el primer número: "))
        y=int(input("Introduzca el segundo número: "))
        print(f"{x}*{y}={x*y}")
        
    elif(opc==4):
        x=int(input("Introduzca el primer número: "))
        y=int(input("Introduzca el segundo número: "))
        print(f"{x}/{y}={x/y}")
        if(y==0):
            print("0 es un numero valido")
        else:
            print("El resto es: ")
    else:
        print("ERROR")
                