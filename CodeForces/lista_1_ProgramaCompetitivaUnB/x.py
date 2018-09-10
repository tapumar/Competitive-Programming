n = int(input())
num = input().split()
div = [0]*n
ind = 0
for i in num:
    i = int(i)
    while(i%2 == 0):
        div[ind] += 1
        i = i/2
    ind += 1
print(min(div))
