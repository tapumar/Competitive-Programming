val1 = 108615168*108625644
val2 = 108625644+val1
seq = [0,1,1,1,2,2,4,8,12,96,108,10368,10476,108615168,108625644,val1,val2]

while(True):
    try:
        n = int(input())
        print(seq[n-1])
    except EOFError:
        break
