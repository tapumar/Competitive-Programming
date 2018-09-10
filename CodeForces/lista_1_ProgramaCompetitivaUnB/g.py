n = input()
din = input().split()
din_int = [int(x) for x in din]
max = max(din_int)
soma = 0
for i in din_int:
    if i < max:
        soma  = soma + (max-i)
print(soma)
