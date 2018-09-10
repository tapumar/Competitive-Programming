a,b = input().split()
a = int(a)
b = int(b)
max = 0
for i in range(a,b+1):
    soma = 0
    for j in str(i):
        if j == "0" or j == "6" or j == "9":
            soma += 1
        elif j == "8":
            soma += 2
    if soma > max:
        max = soma
        num = i
try:
    print(num)
except:
    print(a)
