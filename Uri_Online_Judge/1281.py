casos = int(input())

for i in range(casos):
    total = {}
    soma = 0
    qntDisp = int(input())
    for j in range(qntDisp):
        prod,preco = input().split()
        total[prod] = float(preco)
    
    qntCompra = int(input())
    for k in range(qntCompra):
        prod,qnt = input().split()
        soma += (total[prod]*int(qnt))
    print('R$ %.2f' % soma) 
