import sys

for line in sys.stdin:
    b1 = ((int(line[0])*1)+(int(line[1])*2)+(int(line[2])*3)+(int(line[4])*4)+(int(line[5])*5)+(int(line[6])*6)+(int(line[8])*7)+(int(line[9])*8)+(int(line[10])*9))%11
    if b1 == 10:
        b1 = 0
    b2 = ((int(line[0])*9)+(int(line[1])*8)+(int(line[2])*7)+(int(line[4])*6)+(int(line[5])*5)+(int(line[6])*4)+(int(line[8])*3)+(int(line[9])*2)+(int(line[10])*1))%11
    if b2 == 10:
        b2 = 0
    if b1 == int(line[12]) and b2 == int(line[13]):
        print("CPF valido")
    else:
        print("CPF invalido")
