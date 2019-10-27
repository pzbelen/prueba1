""" Realice un programa que lea por teclado un número entero
positivo N. Debe asegurarse de que el número ingresado sea
positivo. Luego: Calcule y muestre el factorial de los números
desde 1 hasta N """

n = -1
while n < 0:
    n = int(input("Ingrese un valor "))
    
factorial = 1
for a in range (1,n+1):
    factorial *= a

print(factorial)