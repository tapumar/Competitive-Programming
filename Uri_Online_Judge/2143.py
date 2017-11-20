n = int(input())
while(n != 0):
    for i in range(n):
        pessoa = int(input())
        if pessoa%2 == 0:
            print(((pessoa-2)*2)+2)
        else:
            print(((pessoa-1)*2)+1)
    n = int(input())
