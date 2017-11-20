while(True):
  h1,m1,h2,m2 = input().split()
  
  if h1=="0" and m1=="0" and h2=="0" and m2=="0":
    break
  h1 = int(h1)
  h2 = int(h2)
  m1 = int(m1)
  m2 = int(m2)
  
  if h1>h2:
    tempoHora = (24-h1)+h2
    if m2>m1:
      tempoMin = m2-m1
    elif m1>m2:
      tempoHora -= 1
      tempoMin = 60-(m1-m2)
    else:
      tempoMin = 0
  elif h2>h1:
    tempoHora = h2-h1
    if m2>m1:
      tempoMin = m2-m1
    elif m1>m2:
      tempoHora -= 1
      tempoMin = 60-(m1-m2)
    else:
      tempoMin = 0
  else:
    tempoHora = 0
    if m2>m1:
      tempoMin = m2-m1
    elif m1>m2:
      tempoHora = 23
      tempoMin = 60-(m1-m2)
    else:
      tempoHora = 23
      tempoMin = 60
  print((tempoHora*60)+tempoMin)
