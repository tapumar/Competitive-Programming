casos = int(input())
for i in range(casos):
    dieta = input()
    manha = input()
    almoco = input()
    janta = []
    mark = 0
    for j in manha:
        if manha.count(j) > 1 or j in almoco or j not in dieta:
            print("CHEATER")
            mark = 1
            break
            
    if mark == 0:
        for k in almoco:
           if almoco.count(k) > 1 or k not in dieta: 
                print("CHEATER")
                mark = 1
                break
    
    if mark == 0:
        for g in dieta:
            if g not in manha and g not in almoco:
                janta.append(g)
        janta.sort()

        print("".join(janta))
    
