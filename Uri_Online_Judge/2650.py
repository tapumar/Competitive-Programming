todos = {}
qnt,mura = input().split()
mura = int(mura)
qnt = int(qnt)
for i in range(qnt):
    tita = input().split()
    tam = len(tita)
    if int(tita[tam-1]) > mura:
        titan = " ".join(tita[:tam-1])
        print(titan)
