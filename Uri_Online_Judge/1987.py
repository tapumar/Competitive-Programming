while(True):
    try:
        a,b = input().split()
        soma = 0
        for i in range(len(b)):
            soma += int(b[i])
        print(soma,end=" ")
        if soma%3 == 0:
            print("sim")
        else:
            print("nao")
        
    except EOFError:
        break
            
