a,b = input().split()

while(True):
    if a=="0" and b=="0":
        break
    a = int(a)
    b = int(b)
    print((2*a)-b)
    
    a,b = input().split()
