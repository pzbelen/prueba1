""" Realice un programa que lea por teclado tres números enteros
positivos (H, M, S) que contienen hora(s), minuto(s) y
segundo(s) respectivamente, y calcule y muestre el tiempo en
segundos. """

H = int(input("Ingrese horas: "))
M = int(input("Ingrese minutos: "))
S = int(input("Ingrese segundos: "))

HS = H*3600
MS = M*60

T = HS + MS + S

print(T)