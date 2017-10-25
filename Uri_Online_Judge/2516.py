while(True):
    try:
        dist,va,vb = input().split()
        dist = int(dist)
        va = int(va)
        vb = int(vb)
        if va < vb:
            print("impossivel")
        else:
            t = dist/(va-vb)
            print('%.2f' % t)
    except EOFError:
        break
