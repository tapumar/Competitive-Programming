dado = [1,2,3,4,5,6]

casos = int(input())
for i in range(casos):
    l1 = int(input())
    l2,l3,l4,l5 = input().split()
    l6 = int(input())
    teste = [l1,int(l2),int(l3),int(l4),int(l5),l6]
    teste.sort()
    aux = [x for x in range(len(teste)) if teste[x] != dado[x]]
    if l1+l6==7 and int(l2)+int(l4)==7 and int(l3)+int(l5)==7 and not aux:
        print("SIM")
    else:
        print("NAO")
        