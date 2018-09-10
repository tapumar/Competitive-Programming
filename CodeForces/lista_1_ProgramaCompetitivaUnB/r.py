s = input()
p = input()
alf = "abcdefghijklmnopqrstuvwxyz"
for i in s:
    k = alf.index(i)
    print(p[k],end="")
