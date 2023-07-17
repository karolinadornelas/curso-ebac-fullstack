#a estrutura de alteração de fluxo lógico, avalia um valor booleano ou uma comparação
#lógica. seegue identação do código:

#if <booleano/comparação lógica> == True:
#  <faça isso>
#else:
#  <ao contrário, faça isso>
    
#if false:
# print("verdadeiro")
#else:
#  print("Falso")

#exemplo: Código de segurança de um cartão de crédito.

codigo_de_seguranca = '026'
codigo_de_seguranca_cadastrado = '025'

operacao_autorizada = codigo_de_seguranca == codigo_de_seguranca_cadastrado
print(operacao_autorizada)
if operacao_autorizada
  print('pagamento efetuado')
else
  print('Erro: verifique o código informado')

#ou
if codigo_de_seguranca == codigo_de_seguranca_cadastrado
  print('pagamento efetuado')
else
  print('Erro: verifique o código informado')

#exemplo: Código de segurança e senha de um cartão de crédito. aqui, temos de
#analisar duas condições que devem ser verdadeiras para a operação ser aceita.
#temos como base a tabela da verdade:

#|  CÓDIGO  |   SENHA  | | | CÓDIGO OR| |CÓDIGO AND| |   NOT    |
#|          |          | | |  SENHA   | |  SENHA   | |  CÓDIGO  |
#|----------|----------|-|-|----------|-|----------|-|----------|
#| **TRUE** | **TRUE** | | | **TRUE** | | **TRUE** | | FALSE    |
#| **TRUE** | FALSE    | | | **TRUE** | | FALSE    | | FALSE    |
#| FALSE    | FALSE    | | | FALSE    | | FALSE    | | **TRUE** |
#| FALSE    | **TRUE** | | | **TRUE** | | FALSE    | | **TRUE** |

#já que precisamos que ambos código e senha sejam verdadeiros, segue o código:

codigo_de_seguranca = '123'
codigo_de_seguranca_cadastrado = '123'

senha = '0723'
senha_cadastrada = '0723'

if (codigo_de_seguranca == codigo_de_seguranca_cadastrado) & (senha == senha_cadastrada):
  print('pagamento efetuado')
else:
  print('erro: verifique as informações e tente novamente')
  
#ou

if(codigo_de_seguranca != codigo_de_seguranca_cadastrado) | (senha != senha_cadastrada):
  print('erro: verifique as informações e tente novamente')
else:
  print('pagamento efetuado')
  
#para o uso do elif temos:
#if <1° booleano/1° comparação lógica> == True:
#<faça isso se a primeira condição for verdadeira>
#elif <2° booleano/2° comparação lógica> = True:
#<faça isso de a segunda condição for verdadeira>
#else:
#<ao contrario, faça isso>

#para prática, podemos analisar a seguinte tabela:
#|  CÓDIGO  |   SENHA  | | |  CÓDIGO   |          MENSAGEM        |
#           |          | | | AND SENHA |                          |
#|----------|----------|-|-|---------- |--------------------------|
#| **TRUE** | **TRUE** | | | **TRUE**  | Pagamento efetuado       |
#| **TRUE** | FALSE    | | | FALSE     | Erro: Senha inválida     |
#| FALSE    | FALSE    | | | FALSE     | Erro: Código de segurança| 
#                                             e senha inválidos   |
#| FALSE    | **TRUE** | | | FALSE     | Erro: Código de segurança|
#                                                    inválido     |

codigo_de_seguranca = '123'
codigo_de_seguranca_cadastrado = '123'

senha = '0723'
senha_cadastrada = '0723'

if(codigo_de_seguranca == codigo_de_seguranca_cadastrado) & (senha == senha_cadastrada):
    print('pagamento efetuado')
elif (codigo_de_seguranca == codigo_de_seguranca_cadastrado) & (senha != senha_cadastrada):
    print('erro: senha inválida')
elif (codigo_de_seguranca != codigo_de_seguranca_cadastrado) & (senha != senha_cadastrada):
    print('erro: codigo de segurança e senha inválidos)
elif(codigo_de_seguranca != codigo_de_seguranca_cadastrado) & (senha == senha_cadastrada)
    print('erro: codigo de segurança inválido')
