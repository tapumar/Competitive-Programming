casos = int(input())
total = {}
for i in range(casos):
    pessoas = input().split()
    votos = input().split()
    total[1] = votos.count("1")
    total[2] = votos.count("2")
    total[3] = votos.count("3")
    total[4] = votos.count("4")
    total[5] = votos.count("5")
    total[6] = votos.count("6")
    total[7] = votos.count("7")
    total[8] = votos.count("8")
    total[9] = votos.count("9")
    total[10] = votos.count("10") 
    maior = max(total, key=total.get)
    if total[maior] <= len(votos)/2:
        print("-1")
    else:
        print(maior)
