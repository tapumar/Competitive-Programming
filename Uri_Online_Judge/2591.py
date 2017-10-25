casos = int(input())

for i in range(casos):
    poder = input().strip()
    poder = poder.split("e")
    poder = poder[:-1]
    a = poder[0].count("a")
    b = poder[1].count("a")
    total = a*b
    print("k",end="")
    [print("a",end="") for x in range(total)]
    print()
