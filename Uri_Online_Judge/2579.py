lin,col,x,y = input().split()
col = int(col)-1
x = int(x)
y = int(y)

if col%2 != 0:
    if y%2 == 0:
        print("Direita")
    else:
        print("Esquerda")
else:
    if x%2 == 0:
        if y%2 == 0:
            print("Direita")
        else:
            print("Esquerda")
    else:
        if y%2 == 0:
            print("Esquerda")
        else:
            print("Direita")
