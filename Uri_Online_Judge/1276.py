alfa = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
while(True):
    try:
        frase = input()
        resp = []
        nova = []
        for i in frase:
            if i in alfa:
                nova.append(ord(i)-97)
        nova = list(set(nova))
        nova.sort()
        if len(nova) > 0:
            ini = nova[0]
            aux = ini
            fim = 0
            for j in nova:
                if aux+1 == j or aux == j:
                    fim = j
                    aux = j
                    
                else:
                    resp.append(list(alfa.keys())[list(alfa.values()).index(ini+1)]+":"+list(alfa.keys())[list(alfa.values()).index(fim+1)])
                    aux = j
                    ini = j
                    fim = j
            resp.append(list(alfa.keys())[list(alfa.values()).index(ini+1)]+":"+list(alfa.keys())[list(alfa.values()).index(fim+1)])
                  
            for i in range(len(resp)):  
                if i == 0:
                    print(resp[i],end="")
                else:
                    print(", "+resp[i],end="")
        print()
    except EOFError:
        break
