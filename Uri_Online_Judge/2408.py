part = input().split()

if (int(part[0])>int(part[1]) and int(part[0])<int(part[2])) or (int(part[0]) < int(part[1]) and int(part[0])>int(part[2])):
    print(part[0])
elif (int(part[1]) > int(part[0]) and int(part[1])<int(part[2])) or (int(part[1]) < int(part[0]) and int(part[1])>int(part[2])):
    print(part[1])
else:
    print(part[2])
