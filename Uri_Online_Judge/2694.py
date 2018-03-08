casos = int(input())
for i in range(casos):
    soma = 0
    flag = False
    numero = ""
    string = input().strip()
    for j in string:
        if j.isdigit():
            flag = True
            numero += j
        else:
            if flag == True:
                numero = int(numero)
                soma += numero
                numero = ""
                flag = False
    if flag == True:
        numero = int(numero)
        soma += numero
        numero = ""
        flag = False
    print(soma)
