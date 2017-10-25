while(True):
    try:
        frase = input().strip()
        numero = ""
        mark = 0
        for i in frase:
            if ord(i)>=48 and ord(i)<=57:
                numero += i
            elif i == "O" or i == "o":
                numero += "0"
            elif i == "l":
                numero += "1"
            elif i != ',' and i != ' ':
                mark = 1
                
        if numero.isdigit() == True and int(numero) <=2147483647 and mark == 0:
            print(int(numero))
        else:
            print("error")
                
    except EOFError:
        break
