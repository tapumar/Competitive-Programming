n = int(input())
nomes = []
mat = {}
for i in range(n):
    p = input().strip()
    mat[i] = p
    nomes.append(p)
nomes.sort()
for i in range(n):
    print(nomes.index(mat[i]), end=" ")
