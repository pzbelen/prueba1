""" Realice un programa que lea por teclado un número entero
positivo, y lo transforme a número binario (transforme el
número base 10 a base 2). Por ejemplo: 12 ===> 1100 """

n = int(input("Ingrese un valor"))
dividendo = n
cuociente = 0
resto = 0

while dividendo !=0:
    cuociente = dividendo//2
    resto = dividendo%2
    dividendo = cuociente
    
    print(cuociente)