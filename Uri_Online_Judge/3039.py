criancas = int(input())
qtd_carrinhos = 0
qtd_bonecas = 0
for crianca in range(criancas):
    nome, sexo = input().split()
    if sexo == "M":
        qtd_carrinhos += 1
    else:
        qtd_bonecas += 1

print('{} carrinhos'.format(str(qtd_carrinhos)))
print('{} bonecas'.format(str(qtd_bonecas)))
