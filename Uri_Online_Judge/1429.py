from math import factorial
while(True):
    try: 
        acm = input().strip()
        if acm == "0":
            break
        tam = len(acm)-1
        aux = 1
        novo = 0
        while(tam >= 0):
            novo += int(acm[tam])*factorial(aux)
            aux += 1
            tam -= 1
        print(novo)
    except EOFError:
        break
