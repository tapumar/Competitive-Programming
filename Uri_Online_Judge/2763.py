cpf = input()
numero = ""
for i in cpf:
    if i != "." and i != "-":
        numero += i
    else:
        print(numero)
        numero = ""
print(numero)
