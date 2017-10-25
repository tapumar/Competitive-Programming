while(True):
    try:
        n = int(input())
        for i in range(n):
            for j in range(n):
                if i == j and i == int(n/2):
                    print("4",end="")
                elif i >= int(n/3) and j >= int(n/3) and i < n-int((n/3)) and j < n-int((n/3)):
                    print("1",end="")
                elif i == j:
                    print("2",end="")
                elif i+j == n-1:
                    print("3",end="")
                else:
                    print("0",end="")
            print()
        print()
    except EOFError:
        break
