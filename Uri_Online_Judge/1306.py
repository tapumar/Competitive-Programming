i = 1
while(True):
    ruas,num = input().split()
    if ruas == "0" and num == "0":
        break
    ruas = int(ruas)
    num = int(num)
    if ruas == 0 and num == 0:
        break
    teste = ruas/num
    if int(teste) == teste:
        teste = int(teste)-1
    else:
        teste = int(teste)
    teste1 = num*27
    print("Case "+str(i)+":",end=" ")
    if teste1 >= ruas:
        print(teste)
    else:
        print("impossible")
    i += 1
