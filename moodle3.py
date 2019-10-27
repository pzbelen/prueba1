""" Realice un programa que lea por teclado 3 números, y
muestre los valores descendentemente. """

a = int(input("Ingrese un valor: "))
b = int(input("Ingrese un valor: "))
c = int(input("Ingrese un valor: "))

if a>b>c:
    print(a,b,c)
if a>c>b:
    print(a,c,b)
if b>a>c:
    print(b,a,c)
if b>c>a:
    print(b,c,a)
if c>a>b:
    print(c,a,b)
if c>b>a:
    print(c,b,a)