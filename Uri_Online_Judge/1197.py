while(True):
    try:
        v,t = input().split()
        v = int(v)
        t = int(t)
        
        print(v*t*2)
    except EOFError:
        break
