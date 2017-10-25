while(True):
    try:
        c,n = input().split()
        cifra1 = input().strip()
        cifra2 = input().strip()
        for i in range(int(n)):
            frase = input().strip()
            nova = ""
            for j in frase:
                if j.upper() in cifra1:
                    aux = cifra2[cifra1.index(j.upper())]
                elif j.upper() in cifra2:
                    aux = cifra1[cifra2.index(j.upper())]
                else:
                    aux = j
                if j.isupper() == True:
                    nova += aux
                else:
                    nova += aux.lower()
            print(nova)
        print()
    except EOFError:
        break
