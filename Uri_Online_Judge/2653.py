todas = []
while(True):
    try:
        joia = input().strip()
        if joia not in todas:
            todas.append(joia)
        
            
    except EOFError:
        print(len(todas))
        break
