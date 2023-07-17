#exceções são erros que podem acontecer durante a execução de um código
#ex. 
preco = 22.30
pessoas = 0
valor_por_pessoa = preco/pessoas
#resultará em uma mensagem de erro, onde o python informa a linha em que o
#erro se encontra e dá o nome do erro encontrado. nesse caso, o nome do
#erro é ZeroDivisionError: float division by zero; existem outros tipos de
#erro, como o TypeError quando uma tentativa de concatenação é feita entre
#uma string e um valor float por exemplo, já que concatenação só pode ser
#feita entre strings:
nome = 'karolina'
idade = '23'
apresentacao = f'oi, meu nome é' + {nome} + 'e tenho' + {idade} + 'anos.'
print(apresentacao)
#o resultado para isso seria 
TypeError: can only concatenate str (not "set") to str

#estrutura para tratar exceções:

preco = 22.30
pessoas = 0

try:
  valor_por_pessoa = preco / pessoas
  print(valor_por_pessoa)
except ZeroDivisionError:
  print('Número de pessoas inválido. Espera-se um valor maior que 0 e obteve-se um valor igual a ' + str(pessoas))

