casos = int(input())

for i in range(casos):
    idades = input().split()
    cap = int(len(idades)/2)
    print("Case " + str(i+1) + ": " + idades[cap])
