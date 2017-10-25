while(True):
    n = int(input())
    if n == 0:
        break
    todos = []
    mark = 0
    for i in range(n):
        todos.append(input().strip())
    for i in range(len(todos)):
        for j in range(len(todos)):
            if i != j:
                if len(todos[i]) <= len(todos[j]):
                    if todos[i] == todos[j][:len(todos[i])]:
                        mark = 1
                        break         
                else:
                    if todos[j] == todos[i][:len(todos[j])]:
                        mark = 1
                        break
        if mark == 1:
            break
    if mark == 0:
        print("Conjunto Bom")
    else:
        print("Conjunto Ruim")
