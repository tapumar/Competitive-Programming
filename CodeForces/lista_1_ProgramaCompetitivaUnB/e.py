n, max = input().split()
v = input().split()
max = int(max)
ind = 0
for i in range(len(v)):
    if int(v[i]) >= max:
        ind = i+1

if ind == 0:
    print(-1)
else:
    print(ind)
