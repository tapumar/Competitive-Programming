n = int(input())
while(True):
    if n == 0:
        break
    
    for i in range(n):
        k = i
        for j in range(n):
            t = str(2**(k+j))
            f = len(str(2**(n+n-2)))-len(t)
            #print(len(str(2**(k+n-1))))
            for g in range(f):
                print(" ",end="")
            if j<n-1:  
                print(t,end=" ")
            else:
                print(t,end="")
        print()
    print()
        
    n = int(input())
