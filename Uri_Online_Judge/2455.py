pesos = input().split()
esq = int(pesos[0])*int(pesos[1])
dire = int(pesos[2])*int(pesos[3])
if esq == dire:
    print("0")
elif esq > dire:
    print("-1")
else:
    print("1")
    
