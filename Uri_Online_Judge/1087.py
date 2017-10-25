while(True):
    x1,y1,x2,y2 = input().split()
    if x1 == "0":
        break
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if  x1 == x2 and y1 == y2:
        print("0")
    elif x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
        print("1")
    else:
        print("2")
