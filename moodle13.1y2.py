a = 1
b = 2
suma = 0
suma2 = 0
while a<b:
    a = int(input("Ingrese un valor A: "))
    b = int(input("Ingrese un valor B: "))
for c in range (b , a+1):
    if c%2 != 0:
        suma += 1
    else:
        suma2 += 1
        
print("Hay", suma, "numeros pares")
print("Hay", suma2, "numeros impares")