aux = -1
mark = 0
while(True):
    try:
        n = int(input())
        if n <= aux and mark == 0:
            test = aux
            mark = 1
        else:
            aux = n
            
    except EOFError:
        if mark == 1:
            print(test+1)
        else:
            print(aux+1)
        break
