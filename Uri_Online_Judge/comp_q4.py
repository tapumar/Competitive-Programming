casos = int(input())
marc= 0
todos = {}
for i in range(casos):
    num = int(input())
    if num in todos:
        todos[num] += 1
    else:    
        todos[num] = 1
        
for key in sorted(todos):
    print(str(key) + " aparece " +str(todos[key])+" vez(es)")
