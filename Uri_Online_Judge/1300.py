while(True):
    try:
        ang = int(input())
        if ang%6 == 0:
            print("Y")
        else:
            print("N")
    except EOFError:
        break
