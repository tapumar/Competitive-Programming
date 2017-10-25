while(True):
    try:
        n,altmin,altmax = input().split()
        n = int(n)
        altmin = int(altmin)
        altmax = int(altmax)
        cont = 0
        for i in range(n):
            alt = int(input())
            if alt >= altmin and alt <=altmax:
                cont += 1
        print(cont)        
        
    except EOFError:
        break
