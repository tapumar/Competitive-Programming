while(True):
    try:
        n = int(input())
        if n == 0:
            break
        jogos = input().split()
        maria = 0
        joao = 0
        for i in jogos:
            if i == "0":
                maria += 1
            else:
                joao += 1
        print("Mary won "+str(maria)+" times and John won "+str(joao)+" times")   
        
    except EOFError:
        break
