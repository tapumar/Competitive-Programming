while(True):
    try:
        frase = input().split('-')

        if frase[0][0] == 'c' or frase[0][-1] == 'c' or frase[0][0] == 'C' or frase[0][-1] == 'C':
            if frase[1][0] == 'o' or frase[1][-1] == 'o' or frase[1][0] == 'O' or frase[1][-1] == 'O':
                if frase[2][0] == 'b' or frase[2][-1] == 'b' or frase[2][0] == 'B' or frase[2][-1] == 'B':
                    if frase[3][0] == 'o' or frase[3][-1] == 'o' or frase[3][0] == 'O' or frase[3][-1] == 'O':
                        if frase[4][0] == 'l' or frase[4][-1] == 'l' or frase[4][0] == 'L' or frase[4][-1] == 'L':
                            print("GRACE HOPPER")
                        else:
                            print("BUG")
                    else:
                        print("BUG")
                else:
                    print("BUG")
            else:
                print("BUG")
        else:
            print("BUG")
    except EOFError:
        break
