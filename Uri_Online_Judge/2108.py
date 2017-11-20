frase = input().split()
tamMax = 0
MaiorPalavra = ""
while(True):
    marc = 0
    tam = ""
    for palavra in frase:
        if len(palavra) >= tamMax:
            tamMax = len(palavra)
            MaiorPalavra = palavra
        if marc != 0:
            tam = tam + "-"
        tam = tam + str(len(palavra))
        marc = marc+1
    print(tam)
    frase = input().split()
    if frase[0] == "0" and len(frase)== 1:
        break
print()
print("The biggest word: " + MaiorPalavra)
