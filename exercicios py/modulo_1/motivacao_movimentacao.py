#o aplicativo do seu banco registra toda a sua movimentaço financeira. ao final do dia,
#o app consolida o saldo final para que você possa controlar sua vida financeira.

  saldo_inicial_dia_11 = 1000

  dia_11_movimentacao_1 = 150
  dia_11_movimentacao_2 = -50.50
  dia_11_movimentacao_3 = -6.99
  dia_11_movimentacao_4 = 210.95

  dia_11_saldo_final = saldo_inicial_dia_11 + dia_11_movimentacao_1 + dia_11_movimentacao_2 + dia_11_movimentacao_3 + dia_11_movimentacao_4
  print(dia_11_saldo_final)

  #sera que existe uma forma melhor de armazenar as movimentações diárias?
  
  saldo_inicial_dia_11 = 1000

  dia_11_movimentacoes = []

  dia_11_movimentacoes.append(150)
  dia_11_movimentacoes.append(-50.50)
  dia_11_movimentacoes.append(-6.99)
  dia_11_movimentacoes.append(210.95)

  dia_11_saldo_final = saldo_inicial_dia_11 + dia_11_movimentacao_1 + dia_11_movimentacao_2 + dia_11_movimentacao_3 + dia_11_movimentacao_4
  print(dia_11_saldo_final)
