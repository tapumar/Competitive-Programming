while(True):
    try:
        dolar = input()
        cent = input()
        aux = 0
        nova = ""
        if len(dolar)%3 != 0:
            dolar = "$"+ dolar
            aux = 1
        if (len(dolar)-2)%3 == 0:
                dolar = "$"+ dolar
                aux = 2   
        for i in range(len(dolar)):
            if i%3 == 0 and i < len(dolar)-1 and i != 0:
                nova += ","
            nova += dolar[i]
        if len(cent) == 1:
            nova += "."+"0"+cent
        else:
            nova += "."+cent
        if aux == 0:
            nova = "$" + nova
        elif aux == 2:
            nova = nova[1:]
        print(nova)
    except EOFError:
        break
