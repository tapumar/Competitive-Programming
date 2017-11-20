import sys

for line in sys.stdin:
    line = line.split()
    i = int(line[0])
    cont = 0
    while i <= int(line[1]):
        marc = 0
        palavra = str(i)
        for j in palavra:
            if palavra.count(j)>1:
                marc +=1
                break
        
        if marc == 0:
            cont +=1
        i +=1
    print(cont)
