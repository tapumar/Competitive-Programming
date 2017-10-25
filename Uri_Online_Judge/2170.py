k=0
while(True):
    try:
        
        x,y = input().split()
        x = float(x)
        y = float(y)
        k += 1
        i = ((y-x)*100)/x
        print("Projeto "+ str(k)+":")
        print('Percentual dos juros da aplicacao: %.2f' % i,'%')
        print()
    except EOFError:
        break
