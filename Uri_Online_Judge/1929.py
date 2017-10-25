lados = input().split()
lados = [int(x) for x in lados]

if (((abs(lados[0]-lados[1]) < lados[2] and lados[2] < lados[0]+lados[1]) and (abs(lados[0]-lados[2]) < lados[1] and lados[1] < lados[0]+lados[2]) and (abs(lados[2]-lados[1]) < lados[0] and lados[0] < lados[2]+lados[1])) or ((abs(lados[0]-lados[1]) < lados[3] and lados[3] < lados[0]+lados[1]) and (abs(lados[0]-lados[3]) < lados[1] and lados[1] < lados[0]+lados[3]) and (abs(lados[3]-lados[1]) < lados[0] and lados[0] < lados[3]+lados[1])) or ((abs(lados[0]-lados[2]) < lados[3] and lados[3] < lados[0]+lados[2]) and (abs(lados[0]-lados[3]) < lados[2] and lados[2] < lados[0]+lados[3]) and (abs(lados[3]-lados[2]) < lados[0] and lados[0] < lados[3]+lados[2])) or ((abs(lados[1]-lados[2]) < lados[3] and lados[3] < lados[1]+lados[2]) and (abs(lados[1]-lados[3]) < lados[2] and lados[2] < lados[1]+lados[3]) and (abs(lados[3]-lados[2]) < lados[1] and lados[1] < lados[3]+lados[2]))):
    print("S")
else:
    print("N")
