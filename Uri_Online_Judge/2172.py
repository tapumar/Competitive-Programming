n,m = input().split()

while(True):
    if n == "0" and m == "0":
        break
    print(int(n)*int(m))
    n,m = input().split()
