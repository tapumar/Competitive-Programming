casos = int(input())
for i in range(casos):
    mark = 0
    palpite1 = input().strip()
    palpite2 = input().strip()
    teste = input().strip()
    for j in range(len(teste)):
        if teste[j] == "_":
            if mark == 0:
                aux1 = j
            else:
                aux2 = j
            mark = 1

    if palpite1[aux1] == palpite2[aux2] or palpite1[aux2] == palpite2[aux1]:
        print("Y")
    else:
        print("N")
