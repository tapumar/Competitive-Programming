while(True):
    try:
        frase = input()
        mark = 0
        nova = ""
        for i in range(len(frase)):
            if frase[i] != ' ':
                if mark == 0:
                    aux = frase[i].upper()
                    mark = 1
                else:
                    aux = frase[i].lower()
                    mark = 0 
            else:
                aux = ' '
                
            nova += aux
        print(nova)
    except EOFError:
        break
