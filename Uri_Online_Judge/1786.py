import sys

for line in sys.stdin:
    b1 = ((int(line[0])*1)+(int(line[1])*2)+(int(line[2])*3)+(int(line[3])*4)+(int(line[4])*5)+(int(line[5])*6)+(int(line[6])*7)+(int(line[7])*8)+(int(line[8])*9))%11
    if b1 == 10:
        b1 = 0
    b2 = ((int(line[0])*9)+(int(line[1])*8)+(int(line[2])*7)+(int(line[3])*6)+(int(line[4])*5)+(int(line[5])*4)+(int(line[6])*3)+(int(line[7])*2)+(int(line[8])*1))%11
    if b2 == 10:
        b2 = 0
        
        
    print(line[0]+line[1]+line[2]+"."+line[3]+line[4]+line[5]+"."+line[6]+line[7]+line[8]+"-"+str(b1)+str(b2))
