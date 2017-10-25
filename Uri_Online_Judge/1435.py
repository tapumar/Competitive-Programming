while(True):
    num = int(input())
    if num == 0:
        break
    for i in range(num):
        for j in range(num):
            if i+j < num-1:
                print(str(min(i,j)+1).rjust(3),end="")
            elif i+j > num-1:
                print(str(min(num-1-j,num-1-i)+1).rjust(3),end="")
            else:
                if i < num/2:
                    print(str(i+1).rjust(3),end="")
                else:
                    print(str(num-i).rjust(3),end="")

            if j < num-1:
                print(" ",end="")
        print()
    print()
