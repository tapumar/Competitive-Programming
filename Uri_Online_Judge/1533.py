while(True):
    casos = int(input())
    if casos == 0:
        break
    suspeitos = list(map(int,input().split()))
    suspeitos[suspeitos.index(max(suspeitos))] = 0
    print(suspeitos.index(max(suspeitos))+1)
