a1 = int(input())
a2 = int(input())
a3 = int(input())

pri = (a2*2) + (a3*4)
seg = (a1*2) + (a3*2)
ter = (a1*4) + (a2*2)

print(min(pri,seg,ter))
