while(True):
    try:
        n = int(input())
        direita = []
        esq = []
        total = 0
        for i in range(n):
            num,lado = input().split()
            if lado == "D":
                if num in esq:
                    total += 1
                    esq.remove(num)
                else:
                    direita.append(num)
            else:
                if num in direita:
                    total += 1
                    direita.remove(num)
                else:
                    esq.append(num)
        print(total)
                
    except EOFError:
        break
