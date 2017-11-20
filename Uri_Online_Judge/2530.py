while(True):
    try:
      n,m = input().split()
      juan = input().split()
      ric = input().split()
      m = int(m)
      mark = 0
      aux = 0
      for i in juan:
        if i == ric[aux]:
          aux += 1
        if aux >= len(ric)-1:
          mark = 1
          break
          
      if mark == 1:
        print("sim")
      else:
        print("nao")




    except EOFError:
        break
