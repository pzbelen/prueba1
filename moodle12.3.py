""" Realice un programa que lea por teclado un número entero
positivo N. Debe asegurarse de que el número ingresado sea
positivo. Luego: Muestre los primeros N números primos. """

n = -1
while n < 0:
    n = int(input("Ingrese un valor "))

suma2 = 0
i = 2
while suma2 < n:
    suma = 0
    for a in range (2,i):
        if i%a == 0:
            suma += 1
    if suma == 0:
        suma2 += 1
        
        print("El número primo es", i)
    i += 1
        
print(suma2)