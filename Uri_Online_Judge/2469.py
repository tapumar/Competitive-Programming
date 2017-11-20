alunos = int(input())
notas = input().split()
Maior = 0
frequencia = 0
for i in notas:
    cont = notas.count(i)
    i = int(i)
    if cont > frequencia:
        frequencia = cont
        Maior = i
    elif cont == frequencia:
        if Maior<i:
            Maior = i
print(Maior)
