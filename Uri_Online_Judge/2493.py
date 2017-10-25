while(True):
    try:
        n = int(input())
        mark = 0
        ope = {}
        mark = []
        for i in range(n):
            teste = input().split("=")
            teste[0] = teste[0].split(" ")
            if int(teste[0][0]) + int(teste[0][1]) == int(teste[1]): 
                ope[i+1] = "+"
            elif int(teste[0][0]) * int(teste[0][1]) == int(teste[1]):
                ope[i+1] = "*"
            elif int(teste[0][0]) - int(teste[0][1]) == int(teste[1]):
                ope[i+1] = "-"
            else:
                ope[i+1] = "I"    
        for j in range(n):
            pessoa = input().split()
            if ope[int(pessoa[1])] !=  pessoa[2]:
                mark.append(pessoa[0])
        mark.sort()
        if len(mark) == 0:
            print("You Shall All Pass!")
        elif len(mark) == n:
            print("None Shall Pass!")
        else:
            for k in range(len(mark)):
                if k < len(mark)-1:
                    print(mark[k],end=" ")
                else:
                    print(mark[k])
    
    except EOFError:
        break
