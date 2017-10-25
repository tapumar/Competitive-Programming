con1 = input().split()
con2 = input().split()
mark = 0
for i in range(len(con1)):
    if con1[i] == con2[i]:
        mark = 1
        break
if mark == 0:
    print("Y")
else:
    print("N")
