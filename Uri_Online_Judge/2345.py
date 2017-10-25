a1,a2,a3,a4 = input().split()
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
a4 = int(a4)
team = [abs((a1+a2)-(a3+a4)),abs((a1+a3)-(a2+a4)),abs((a1+a4)-(a2+a3))]
print(min(team))
