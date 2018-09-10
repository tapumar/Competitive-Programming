ano = int(input())
while(True):
    ano += 1
    t = set(str(ano))
    if len(t) == len(str(ano)):
        print(ano)
        break
