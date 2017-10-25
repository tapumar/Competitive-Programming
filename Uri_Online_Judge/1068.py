while(True):
    try:
        parenteses = []
        exp = input().strip()
        mark = 0
        for i in exp:
            if i == "(":
                parenteses.append(i)
            elif i == ")":
                if not parenteses:
                    mark = 1
                    break
                else:
                    parenteses.pop()
                    
        if mark == 0 and not parenteses:
            print("correct")
        else:
            print("incorrect")
        
    except EOFError:
        break
