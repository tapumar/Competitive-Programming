while True:
    try:
        cont = 0
        alien = input().strip()
        frase = input().strip()
        for letra in frase:
            if alien.find(letra)>=0:
                cont = cont+1
        print(cont)
    except EOFError:
        break
