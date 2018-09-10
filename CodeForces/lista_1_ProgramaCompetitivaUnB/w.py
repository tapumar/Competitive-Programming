n,a,b = input().split()
n = int(n)
a = int(a)
b = int(b)
soma = 0
for i in range(1,n+1):
    s = 0
    for k in str(i):
        s += int(k)
    if s >= a and s <= b:
        soma += i
print(soma)
