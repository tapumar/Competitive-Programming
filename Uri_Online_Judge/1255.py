n = int(input())
for i in range(n):
    qnt = {}
    frase = input().strip()
    frase = frase.lower()
    esse = []
    for j in frase:
        if ord(j) >= 97 and ord(j)<=122:
            if j in qnt:
                qnt[j] += 1
            else:
                qnt[j] = 1
    maior = max(qnt.values())
    for j in qnt:
        if qnt[j] == maior:
            esse.append(j)
    esse.sort()
    for k in esse:
        print(k,end="")
    print()
