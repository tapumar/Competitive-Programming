while(True):
    try:
        s = input().strip()
        t = input().strip()
        maior = 0
        tam = 0
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                aux = s[i:j]
                if aux not in t:
                    break
                else:
                    tam = len(aux)
            if tam > maior:
                maior = tam
        print(maior)
    except EOFError:
        break
        
