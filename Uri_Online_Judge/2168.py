n = int(input())
matrix = []
for i in range(n+1):
    linha =  input().split()
    matrix.append(linha)
for j in range(1,n+1):
    for k in range(1,n+1):
        seg = 0
        if matrix[j][k] == "1":
            seg += 1
        if matrix[j][k-1] == "1":
            seg += 1
        if matrix[j-1][k] == "1":
            seg += 1
        if matrix[j-1][k-1] == "1":
            seg += 1
        if seg >= 2:
            print("S",end="")
        else:
            print("U",end="")
    print()
