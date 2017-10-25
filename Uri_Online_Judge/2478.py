part = int(input())
todos = {}
for i in range(part):
    nome = input().split()
    todos[nome[0]] = nome[1:]
while(True):
    try:
        pessoa = input().split()
        if pessoa[0] in todos:
            if pessoa[1] in todos[pessoa[0]]:
                print("Uhul! Seu amigo secreto vai adorar o/")
            else:
                print("Tente Novamente!")
        else:
            print("Tente Novamente!")
            
    except EOFError:
        break
