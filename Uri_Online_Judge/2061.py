abas,casos = map(int,input().split(' '))
aberto = abas
for i in range(casos):
    acao = input()
    if acao == 'fechou':
        aberto = aberto + 1
    elif acao == 'clicou':
        aberto = aberto - 1
print(aberto)
