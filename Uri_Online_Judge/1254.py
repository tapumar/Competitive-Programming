while(True):
    try:
        original = input()
        subst = input()
        codigo = input()
        tag = ""
        mark = 0
        novo = ""
        for i in codigo:
            if i == "<":
                mark = 1
                novo += i
            elif i == ">":
                while(True):
                    teste = tag.lower().find(original.lower())
                    if teste == -1:
                        break
                    tag = tag[:teste]+subst+tag[(teste+len(original)):]
                novo += tag + ">"
                tag = ""
                mark = 0
            elif mark == 1:
                tag += i
            else:
                novo += i
        print(novo)
    except EOFError:
        break
