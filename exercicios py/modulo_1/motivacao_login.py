#motivação 
#em websites (redes sociais, e-commerce, sites corporativos, etc.) 
#é comum o uso de sistemas de controle de acesso (login). Em geral, nesses sistemas
#o usuário fonrnece dois dados: usuário e senha:

  #usuario = 'karolina.dornelas'
  #senha = 'lemonzest321'

#do lado do servidor, o backend do site tem armazenados os dados de um usuário e senha
#fornecidos pelo usuário no momento do cadastro:

  #usuario_cadastrado = 'karolina.dornelas'
  #senha_cadastrada = 'lemonzest321'

#como comparamos se as string são iguais para conceder ou bloquear o acesso do usuario?

  #compara se os dados fornecidos pelo usuário são iguais aos dados do cadastro:
  usuario = 'karolina.dornelas'
  senha = 'lemonzest321'

  usuario_cadastro = 'kaorlina.dornelas'
  senha_cadastro = 'lemonzest321'

  usuario_valido = usuario == usuario_cadastro
  senha_valido = senha == senha_cadastro

  print(usuario_valido)
  print(senha_valido)

  #decide se concede o acesso:
  acesso_permitido = usuario_valido & senha_valido
  print(acesso_permitido)
