casos = int(input())
for i in range(casos):
    p1=0
    p=0
    bonus = int(input())
    a1,d1,l1 = map(int,input().split(' '))
    a,d,l = map(int,input().split(' '))
    if l1%2 == 0:
        p1 = p1+bonus
    if l%2 == 0:
        p = p+bonus
    p1 = p1 + (a1+d1)/2
    p = p + (a+d)/2
    if p < p1:
        print("Dabriel")
    elif p > p1:
        print("Guarte")
    else:
        print("Empate")
