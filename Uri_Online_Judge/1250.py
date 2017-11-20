casos = int(input())

for i in range(casos):
    
    num = int(input())
    atingido = 0
    tiros = [x for x in input().split()]
    pulos = input().strip()
    for j in range(len(pulos)):
        if (pulos[j] == "S" and int(tiros[j])<=2) or (pulos[j] == "J" and int(tiros[j]) >2):
            atingido += 1
    print(atingido)
