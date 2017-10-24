while(True):
    try:
        tam = int(input())
        esp = int(tam/2)
        fol = 1
        for i in range(int(tam/2)+1):
            [print("",end=" ") for x in range(esp)]
            [print("*",end="") for x in range(fol)]
            print()
            esp -= 1
            fol += 2
        [print("",end=" ") for x in range(int(tam/2))]
        print("*")
        [print("",end=" ") for x in range(int(tam/2)-1)]
        print("***")
        print()
    except EOFError:
        break
