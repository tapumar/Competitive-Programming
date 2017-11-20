while(True):
    frase = input().strip()
    if frase == "*":
        break
    frase = frase.split()
    marc = 0
    aux = ""
    marc1 = 0
    for palavra in frase:
        if marc == 0:
            aux = palavra[0]
            marc = 1
        else:
            if palavra[0] != aux.upper() and palavra[0] != aux.lower():
                marc1 = 1
                break
    if marc1 == 1:
        print("N")
    else:
        print("Y")
