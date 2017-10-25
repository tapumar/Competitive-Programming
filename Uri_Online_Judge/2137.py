import sys 
while(True):
    try:
        ordem = []
        caso = int(input())
        for i in range(caso):
            esse = int(input())
            ordem.append(esse)
        ordem.sort()
        for j in range(len(ordem)):
            if len(str(ordem[j])) == 1:
                print("000"+str(ordem[j]))
            elif len(str(ordem[j])) == 2:
                print("00"+str(ordem[j]))
            elif len(str(ordem[j])) == 3:
                print("0"+str(ordem[j]))
            else:
                print(str(ordem[j]))
    except EOFError:
        break
