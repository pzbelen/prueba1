""" Realice un programa que lea por teclado un texto, e indique:
Cuántos dígitos posee en total. Por ejemplo, el texto "hola 45,
mundo 56" posee 4 dígitos en total."""
texto = input("Ingrese un texto: ")
suma = 0

for c in texto:
    if c == "0" or c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c ==  "8" or c == "9":
        suma = suma + 1
        
print("el texto contiene", suma ,"digitos") 