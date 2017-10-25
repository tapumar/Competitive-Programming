while(True):
    try:
        todos,est = input().split()
        valores = input().split()
        todos = int(todos)
        est = int(est)
        valores = [int(x) for x in valores]
        valores.sort()
        soma = 0
        for i in valores[len(valores)-est:]:
            soma += int(i)
        print(soma)
    except EOFError:
        break
        
