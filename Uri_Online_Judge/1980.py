while(True):
    s = input().strip()
    if s == "0":
        break
    tam = len(s)
    total = 1
    while(tam>1):
        total *= tam
        tam -= 1
    print(total)
