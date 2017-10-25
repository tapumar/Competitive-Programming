while(True):
    part,prob = input().split()
    if part == "0" and prob == "0":
        break
    part = int(part)
    prob = int(prob)
    todos = []
    for i in range(part):
        todos.append(input().split())
    soma1 = 0
    soma2 = 0
    soma3 = 0
    soma4 = 0

    for j in todos:
        aux = 0
        for k in j:
            if k == "1":
                aux+= 1
        if aux == prob:
            soma1 = 1
        elif aux == 0:
            soma4 = 1
    
    for n in range(prob):
        aux = 0
        aux1 = 0
        for m in todos:
            if m[n] == "0":
                aux += 1
            if m[n] == "1":
                aux1 += 1
        if aux == part:
            soma3 = 1
        elif aux1 == part:
            soma2 = 1
    tam = 0    
    for g in [soma1,soma2,soma3,soma4]:
        if g == 0:
            tam += 1
    print(tam)
