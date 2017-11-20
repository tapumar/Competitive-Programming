casos = int(input())

for i in range(casos):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cont = 0
    frase = input().strip()
    for letra in frase:
        if alfabeto.find(letra) >= 0:
           alfabeto = alfabeto.replace(letra, "")
    if len(alfabeto) == 0:
        print("frase completa")
    elif len(alfabeto) <= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")
