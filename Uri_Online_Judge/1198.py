while(True):
    try:
        ha,opo = input().split()
        ha = int(ha)
        opo = int(opo)
        if ha>opo:
            print(ha-opo)
        else:
            print(opo-ha)
    except EOFError:
        break
