casos = int(input())

while(True):
    if casos == 0:
        break
    varetas = 0
    for i in range(casos):
        var, num = input().split()
        num = int(num)
        if num%2 != 0:
            num -=1
        varetas += num
    if varetas%4 != 0:
        varetas -= 2
    print(int(varetas/4))
        
    casos = int(input())
