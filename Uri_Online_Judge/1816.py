num = int(input())
k = 1
while(True):
    if num == 0:
        break
    codigo = input().split()
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nova = ""
    for i in codigo:
        aux = alf[int(i)-1]
        alf = alf.replace(alf[int(i)-1],'')
        nova += aux
        alf = aux+alf
    print("Instancia "+ str(k))
    print(nova)
    print()
    k += 1
    num = int(input())
