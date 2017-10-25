n = int(input())
par = []
impar = []
for i in range(n):
    num = int(input())
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
impar = impar[::-1]
[print(x) for x in par]
[print(x) for x in impar]
