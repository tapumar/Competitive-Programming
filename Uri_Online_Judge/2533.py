while(True):
    try:
        dis = int(input())
        somaNota = 0
        somaCarga = 0
        for i in range(dis):
            nota,carga = input().split()
            somaNota += (int(nota)*int(carga))
            somaCarga += int(carga)
            
        ira = somaNota/(somaCarga*100)
        
        print('%.4f' % ira)
        
    except EOFError:
        break
