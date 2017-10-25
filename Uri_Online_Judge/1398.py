while(True):
    try:
        linha = ""
        line = input().strip()
        linha += line
        while(line[-1] != "#"):
            line = input().strip()
            linha += line
        linha = linha.strip("#")
        linha = int(linha,2)
        if linha%131071 == 0:
            print("YES")
        else:
            print("NO")        
    except EOFError:
        break
