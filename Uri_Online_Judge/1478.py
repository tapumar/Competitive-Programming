while(True):
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        for j in range(n):
            if j<n-1:
                if j==i:
                    print("1".rjust(3),end=" ")
                elif j>i:
                    print(str(j-i+1).rjust(3),end=" ")
                else:
                    print(str(i-j+1).rjust(3),end=" ")
            else:
                if j==i:
                    print("1".rjust(3))
                elif j>i:
                    print(str(j-i+1).rjust(3))
                else:
                    print(str(i-j+1).rjust(3))
    print()
