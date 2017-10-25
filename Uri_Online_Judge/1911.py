while(True):
    n = int(input())
    if n == 0:
        break
    original = {}
    soma = 0
    for i in range(n):
        a,b = input().split()
        original[a] = b
    m = int(input())

    for i in range(m):
        aux = 0
        a,b = input().split()
        for j in range(len(b)):
            if original[a][j] != b[j]:
                aux += 1
        if aux > 1:
            soma += 1
            
    print(soma)
