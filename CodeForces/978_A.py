n = int(input())

seq = input().split()
rep = []
for i in seq:
    if i not in rep:
        rep.append(i)
    else:
        rep.remove(i)
        rep.append(i)
print(len(rep))
for j in rep:
    if rep.index(j) == len(rep)-1:
        print(j)
    else:
        print(j, end=' ')
