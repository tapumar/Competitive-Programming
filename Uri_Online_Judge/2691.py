casos = int(input())

for i in range(casos):
    um,dois = input().split('x')
    um = int(um)
    dois = int(dois)

    if um != dois:
        print(um,"x 5 =",um*5,"&&",dois,"x 5 =",dois*5)
        print(um,"x 6 =",um*6,"&&",dois,"x 6 =",dois*6)
        print(um,"x 7 =",um*7,"&&",dois,"x 7 =",dois*7)
        print(um,"x 8 =",um*8,"&&",dois,"x 8 =",dois*8)
        print(um,"x 9 =",um*9,"&&",dois,"x 9 =",dois*9)
        print(um,"x 10 =",um*10,"&&",dois,"x 10 =",dois*10)
    else:
        print(um,"x 5 =",um*5)
        print(um,"x 6 =",um*6)
        print(um,"x 7 =",um*7)
        print(um,"x 8 =",um*8)
        print(um,"x 9 =",um*9)
        print(um,"x 10 =",um*10)
