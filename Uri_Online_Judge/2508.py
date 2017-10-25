letras = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":1,"K":2,"L":3,"M":4,"N":5,"O":6,"P":7,"Q":8,"R":9,"S":1,"T":2,"U":3,"V":4,"W":5,"X":6,"Y":7,"Z":8}

while(True):
    try:
        nome = input().strip()
        num = 0
        pont = 0
        nome = nome.upper()
        for i in nome:
            if i in letras:
                num += letras[i]
        soma = num
        while(len(str(soma)) > 1):
            num = 0
            for j in str(soma):
                num += int(j)
            soma = num
        print(soma)

    except EOFError:
        break
