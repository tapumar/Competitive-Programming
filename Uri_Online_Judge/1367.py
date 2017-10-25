num = int(input())
while(True):
    if num == 0:
        break
    id = 1
    prob = {}
    tempo = {}
    for i in range(num):
        caso = input().split()
        if caso[0] in prob:
            if caso[2] == "correct":
                 if prob[caso[0]] != 1:
                    prob[caso[0]] = 1
                    tempo[caso[0]] += int(caso[1])
            else:
                if prob[caso[0]] != 1:
                    tempo[caso[0]] += 20
                
        else:
            if caso[2] == "correct":
                prob[caso[0]] = 1
                tempo[caso[0]] = int(caso[1])
            else:
                prob[caso[0]] = 0
                tempo[caso[0]] = 20
       
    soma = 0
    certo = [x for x in prob if prob[x] == 1]
    for j in certo:
        soma+=tempo[j]
        
    print(len(certo),soma)
           
    num = int(input())
