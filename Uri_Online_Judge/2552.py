while(True):
    try:
        matriz = []
        n,m = input().split()
        n = int(n)
        for i in range(n):
            matriz.append(input().split())
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == "1":
                    print("9",end="")
                else:
                    soma = 0
                    if j != 0 and matriz[i][j-1] == "1":
                        soma += 1
                    if j!= len(matriz[i])-1 and matriz[i][j+1] == "1":
                        soma += 1
                    if i != 0 and matriz[i-1][j] == "1":
                        soma += 1
                    if i != len(matriz)-1 and matriz[i+1][j] == "1":
                        soma += 1
                        
                    print(soma,end="")
            print()
    except EOFError:
        break
