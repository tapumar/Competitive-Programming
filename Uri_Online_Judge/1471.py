while(True):
    try:
        foi,voltou = input().split()
        foi = int(foi)
        voltaram = [int(x) for x in input().split()]
        foram = [x for x in range(1,foi+1)]
        ident = []
        for i in foram:
            if i not in voltaram:
                ident.append(i)
        if len(ident) == 0:
            print("*",end="")
        else:
            ident.sort()
            [print(x,end=" ") for x in ident]
        print()
        
    except EOFError:
        break
