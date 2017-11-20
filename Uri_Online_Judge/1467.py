while(True):
    try:
        a,b,c = input().split()
        if a!=b and a!=c:
            print("A")
        elif b!=a and b!=c:
            print("B")
        elif c!=a and c!=b:
            print("C")
        else:
            print("*")
        
    except EOFError:
        break
