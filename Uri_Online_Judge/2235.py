c1,c2,c3 = map(int,input().split(' '))
if c1 == c2+c3 or c2 == c1+c3 or c3 == c1+c2 or c1 == c2 or c2==c3 or c1==c3 or c2==0 or c1==0 or c3==0:
    print("S")
else:
    print("N")
