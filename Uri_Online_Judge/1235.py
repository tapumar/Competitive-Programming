num = int(input())

for i in range(num):
    frase = input()
    tam = len(frase)
    sub1 = frase[:int(tam/2)]
    sub2 = frase[int(tam/2):]
    sub1 = sub1[::-1]
    sub2 = sub2[::-1]
    print(sub1,end="")
    print(sub2)
    
