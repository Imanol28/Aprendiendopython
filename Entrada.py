Valor = input()
print(type(Valor))

ValorEntero = (Valor.isdigit() and Valor.find(".")==-1)

if (ValorEntero) :
    print ("Dato entero. ¡Muy bien!")
else:
    print("Dato no es entero. Intentar nuevamente.")
© 2019 GitHub, Inc.