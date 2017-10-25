soma = 0
while(True):
    try:
        corvo = input().strip()
        num = ""
        if corvo == "caw caw":
            print(soma)
            soma = 0
        else:
            if corvo[0] == "*":
                num += "1"
            elif corvo[0] == "-":
                num += "0"
            if corvo[1] == "*":
                num += "1"
            elif corvo[1] == "-":
                num += "0"
            if corvo[2] == "*":
                num += "1"
            elif corvo[2] == "-":
                num += "0"
            soma += int(num,2)
                 
    except EOFError:
        break
