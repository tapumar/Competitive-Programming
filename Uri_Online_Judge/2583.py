casos = int(input())
for i in range(casos):
    qnt = int(input())
    tudo = []
    for j in range(qnt):
        coisa = input().split()
        if coisa[1] == "chirrin" and coisa[0] not in tudo:
            tudo.append(coisa[0])
        elif coisa[1] == "chirrion" and coisa[0] in tudo:
            tudo.remove(coisa[0])
    print("TOTAL")
    tudo.sort()
    for k in tudo:
        print(k)
