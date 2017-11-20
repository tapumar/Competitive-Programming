while(True):
    try:
        line = input().strip()
        line2 = input().strip()
        if line.find(line2) >= 0:
            print("Resistente")
        else:
            print("Nao resistente")
    except EOFError:
        break
