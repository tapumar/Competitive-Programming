casos = int(input())

for i in range(casos):
    x,y = input().split()
    area = int((int(x)*int(y))/2)
    print(str(area) + " cm2")
