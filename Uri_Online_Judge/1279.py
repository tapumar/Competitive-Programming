import sys

esse = 0
for line in sys.stdin:
    aux = 0
    aux1 = 0
    aux2 = 0
    line = int(line)
    if esse != 0:
        print()
    esse = esse+1
    if line%4 == 0:
        if line%100 != 0:
            aux = 1
            print("This is leap year.")
    if line%400 == 0:
        aux = 1
        print("This is leap year.")
    if line%15 == 0:
        aux2 = 1
        print("This is huluculu festival year.")
    if aux == 1 and line%55 == 0:
        aux1 = 1
        print("This is bulukulu festival year.")
        
    elif aux == 0 and aux1 == 0 and aux2 == 0:
        print("This is an ordinary year.")
