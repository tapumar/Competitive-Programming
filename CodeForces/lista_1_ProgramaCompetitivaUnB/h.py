n,k = input().split()
k = int(k)
velas = int(n)

check = 0
while(velas > 0):
    if check%k != 0:
        velas = velas - 1
    check = check + 1
print(check-1)
