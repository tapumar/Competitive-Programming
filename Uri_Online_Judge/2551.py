while(True):
    try:
        maior = 0
        treinos = int(input())
        for i in range(treinos):
            dura,dist = input().split()
            dura = int(dura)
            dist = int(dist)
            if (dist/dura) > maior:
                maior = dist/dura
                print(i+1)

             
        
    except EOFError:
        break
        
