import math
t = int(input())
for i in range(t):
    c,d = input().split()
    c = int(c)
    d = int(d)
    if c == 0 and d == 0:
        print("0")
    else:
        total = math.pow(26,c) * math.pow(10,d)
        print(int(total))
