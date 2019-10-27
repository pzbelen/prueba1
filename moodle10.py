""" Realice un programa que determine si un número entero
positivo es perfecto. """

N = int(input("Ingrese un valor: "))
suma = 0

for a in range (1,N):
    if N%a == 0:
        suma += a
if suma == N:
    print("El valor es un numero perfecto")
    
else:
    print("El valor no es un numero perfecto")