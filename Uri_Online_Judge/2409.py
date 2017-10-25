a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

h,l = input().split()
h = int(h)
l = int(l)
marc = 0
if a < h:
    if b < l or c < l:
        marc = 1
if b< h:
    if a<l or c<l:
        marc =1
if c<h:
    if a<l or b<l:
        marc =1
if marc == 1:
    print("S")
else:
    print("N")
