dist = 0
amigos = 0
while(True):
    try:
       
        nome = input().strip()
        aux = int(input())
        dist += aux
        amigos += 1
        
    except EOFError:
        media = dist/amigos
        print('%.1f' % media)
        break
