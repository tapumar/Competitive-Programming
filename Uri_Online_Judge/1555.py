from math import pow

casos = int(input())

for i in range(casos):
    x,y = input().split()
    x = int(x)
    y = int(y)
    
    Rafael = pow((3*x),2) + pow(y,2)
    Beto = (2*pow(x,2)) + pow((5*y),2)
    Carlos = pow(y,3) - (100*x)
    if Rafael > Beto and Rafael > Carlos:
        print("Rafael ganhou")
    elif(Beto > Rafael and Beto > Carlos):
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
