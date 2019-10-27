suma = 0
N = 4000000
a = 0
b = 1
for i in range ( 1 , N ):
    b = b + a
    a = b - a
    if a%2 == 0:
        suma = suma + a
    if a > N:
        break
print(suma)    