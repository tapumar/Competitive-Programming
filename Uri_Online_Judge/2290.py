while(True):
    try:
        n = int(input())
        if n == 0:
            continue
        lista = input().split()
        lista.sort()
        check = 0
        love = []
        anterior = 0
        first = True
        for i in lista:
            if first:
                first = False
                check = 1
            elif i != anterior and check < 2:
                love.append(anterior)
                check = 1
            elif i != anterior and check == 2:
                check = 1
            elif i == anterior and check < 2:
                check += 1
            elif i == anterior and check == 2:
                check = 1
            anterior = i
        if len(love)< 2 and lista[-2] != anterior and check < 2:
            love.append(anterior)
        if len(love) <2 and lista[-2] == anterior and check <= 2:
            love.append(anterior)
        love = [int(x) for x in love]
        love.sort()
        print(love[0],end=' ')
        print(love[1])
    except:
        break
