while(True):
    try:
        frase = input()
        nova = ""
        mark = 0
        mark1 = 0
        for i in frase:
            if i == "_":
                if mark == 0:
                    aux = "<i>"
                    mark = 1
                else:
                    aux = "</i>"
                    mark = 0
            elif i == "*":
                if mark1 == 0:
                    aux = "<b>"
                    mark1 = 1
                else:
                    aux = "</b>"
                    mark1 = 0
            else:
                aux = i
            nova += aux
        print(nova)
    except EOFError:
        break
