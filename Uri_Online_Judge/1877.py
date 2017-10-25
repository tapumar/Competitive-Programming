n,k = input().split()
torres = input().split()
n = int(n)
k = int(k)
aux = 0
mark = 0
pico = 0
vale = 0
for i in torres:
    i = int(i)
    if i < aux and mark == 0:
        pico += 1
        mark = 1
    elif i > aux and mark == 1:
        vale += 1
        mark = 0
    aux = i
if pico == k and vale == k-1:
    print("beautiful")
else:
    print("ugly")
