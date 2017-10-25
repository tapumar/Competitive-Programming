while(True):
    try:
        n,d = input().split()
        n = int(n)
        d = int(d)
        mark = 0
        for i in range(d):
            dia = input().strip()
            dia = dia.split(" ")
            pessoas = dia[1:].count("1")
            if pessoas == n and mark == 0:
                mark = 1
                diaD = dia[0]
        if mark == 1:
            print(diaD)
        else:
            print("Pizza antes de FdI")
    except EOFError:
        break
