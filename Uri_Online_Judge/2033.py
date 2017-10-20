while(True):
  try:
    emp = float(input())
    juros = float(input())
    meses = int(input())
    
    simples = emp + meses*(juros*emp)
    composto = emp
    for i in range(meses):
      composto = composto + juros*composto
    
    print("DIFERENCA DE VALOR = ",end="")
    print('%.2f' % (abs(composto-simples)))
    print("JUROS SIMPLES = ",end="")
    print('%.2f' % (simples-emp))
    print("JUROS COMPOSTOS = ",end="")
    print('%.2f' % (composto-emp))
  except EOFError:
    break