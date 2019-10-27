""" Realice un programa que muestre los números perfectos entre
1 y 1000. """

  
N = 1000
for i in range (1,N):
    suma = 0
    for a in range (1,i):
        if i%a == 0:
            suma += a
    if suma == i:
        print(i)