casos = int(input())

for i in range(casos):
    din,n = input().split()
    din = int(din)
    valor = input().split()
    maior = 0

    for j in valor:
        j = float(j)
        qnt = int(din/j)
        if din-(qnt*float(j)) > maior and j<=din:
            maior = din-(qnt*float(j))
         
    print('%.2f' % maior)
