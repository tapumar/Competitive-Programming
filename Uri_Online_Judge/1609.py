casos = int(input())

for i in range(casos):
    n = int(input())
    carneiros = input().split()
    carneiros = list(set(carneiros))
    print(len(carneiros))
    
