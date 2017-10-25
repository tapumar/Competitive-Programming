casos = int(input())

for i in range(casos):
    a,b = input().split()
    if b == a[(len(a)-len(b)):]:
        print("encaixa")
    else:
        print("nao encaixa")
