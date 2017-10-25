num = int(input())
mark = 1
while(True):
    if num == 0:
        break
        
    if mark != 1:
        print()

    todos = []
    maior = 0
    for i in range(num):
        todos.append(input().strip())
        
    maior = max(todos, key=len)
    
    for j in todos:
        print(j.rjust(len(maior),' ')) 
        
    mark+=1    
    num = int(input())
