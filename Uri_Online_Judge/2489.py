from math import tan,radians
while(True):
    try:
        alt,dist,ang = input().split()
        alt = float(alt)
        dist = float(dist)
        ang = radians(90-float(ang))
        co = tan(ang)*dist
        co = alt - co
        print('%.4f' % co)

    except EOFError:
        break
    
