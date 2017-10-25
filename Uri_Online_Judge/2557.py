while(True):
    try:
        novo = []
        eq = input().strip()
        eq1 = eq.split('+')
        novo.append(eq1[0])
        eq1 = eq1[1].split('=')
        novo.append(eq1[0])
        novo.append(eq1[1])
        if "R" in novo:
            print(int(novo[2])-int(novo[1]))
        elif "L" in novo:
            print(int(novo[2])-int(novo[0]))
        else:
            print(int(novo[0])+int(novo[1]))

            
    except EOFError:
        break
