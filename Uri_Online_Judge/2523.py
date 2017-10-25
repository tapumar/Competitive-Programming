while(True):
    try:
        j = 1
        novo = {}
        base = input().strip()
        for i in base:
            novo[j] = i
            j+=1
        n = int(input())
        lamp = input().split()
        for k in lamp:
            print(novo[int(k)],end="")
        print()
        
    except EOFError:
        break
