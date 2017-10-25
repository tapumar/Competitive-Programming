import math

while(True):
    try:
        a,b,c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)

        p = (a+b+c)/2

        areaT = math.sqrt(p*(p-a)*(p-b)*(p-c))

        RaioMenor = areaT/p


        areaMenor = 3.1415926535897*(RaioMenor**2)

        areaMaior = 3.1415926535897*(((a*b*c)/(math.sqrt((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))))**2)

        areaMaior = areaMaior-areaT

        areaT = areaT-areaMenor
        print('%.4f' % areaMaior,end=" ")
        print('%.4f' % areaT,end=" ")
        print('%.4f' % areaMenor)
        
    except EOFError:
        break
