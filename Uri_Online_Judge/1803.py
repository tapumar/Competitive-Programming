linha1 = input().strip()
linha2 = input().strip()
linha3 = input().strip()
linha4 = input().strip()
saida = ""
f = linha1[0]+linha2[0]+linha3[0]+linha4[0]
l = linha1[-1]+linha2[-1]+linha3[-1]+linha4[-1]
i=1
while(i<len(linha1)-1):
    num = linha1[i]+linha2[i]+linha3[i]+linha4[i]
    saida = saida+chr(((int(f)*int(num))+int(l))%257)
    i+=1
print(saida)
