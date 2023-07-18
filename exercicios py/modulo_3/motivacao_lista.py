#E1. Faça um programa que peça um número e então mostre a mensagem 'o numero informado foi [numero]'.
numero_escolhido = input('Escolha um número: ')
print('O número escolhido foi:'+ numero_escolhido)

#E2. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e 
#mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
temperatura_fahrenheit = (float(input('Insira a temperatura em graus Fahrenheit: ')))
temperatura_celsius = 5 * ((temperatura_fahrenheit - 32)/9)
print(f'A temperatura {temperatura_fahrenheit}F° em Celsius é: {temperatura_celsius:.2f}C°')

#E3. Escreva um programa que simule uma funcionalidade de login, validando as
#informações em 3 condições: Bem vindo (usuario); Senha Incorreta ou Usuário não encontrado
senha_cadastrada = 1807
username_cadastrado = 'karol'
senha = input('Digite sua senha: ')
senha = int(senha)
username = input('Username: ')
if senha == senha_cadastrada and username == username_cadastrado:
    print('Bem-vindo,', username)
elif senha != senha_cadastrada and username == username_cadastrado:
    print('Senha inválida')
else:
    print('Usuário não encontrado. Por favor, revise os dados ou crie uma conta.')

#E4. Faça um programa que peça dois numeros e imprima a soma
NUM_1 = input('informe o primeiro número: ')
NUM_1 = int(NUM_1)
NUM_2 = input('informe o segundo número: ')
NUM_2 = int(NUM_2)
resultado = NUM_1 + NUM_2
resultado = str(resultado)
print('a soma resulta em: ' + resultado)

#E5. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
NOTA_1 = float(input('informe a primeira nota: '))
NOTA_2 = float(input('informe a segunda nota: '))
NOTA_3 = float(input('informe a terceira nota: '))
NOTA_4 = float(input('informe a quarta nota: '))
MEDIA = ((NOTA_1 + NOTA_2 + NOTA_3 + NOTA_4)/4)
MEDIA = str(MEDIA)
print('A sua média total é:' + MEDIA)
MEDIA = float(MEDIA)
if(MEDIA >= 7):
  print('APROVADO')
elif(MEDIA > 5 and MEDIA < 7):
  print('RECUPERAÇÃO')
else:
    print('REPROVADO')
  
#E6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salario_por_hora = (float(input('Valor da hora trabalhada: ')))
horas_trabalhadas_mes = (float(input('Quantas horas você trabalha por mês: ')))
salario_mes = salario_por_hora * horas_trabalhadas_mes
print(f'Seu salário do mês é: R$ {salario_mes:.2f}')

#E7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,  
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
#5% para o sindicato, faça um programa que nos dê: salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
usuario_valor = (float(input('Insira o valor da sua hora trabalhada: ')))
usuario_hora = (float(input('Insira o quantidade de horas trabalhadas no mês: ')))

salario_bruto = usuario_valor * usuario_hora
salario_bruto =str(salario_bruto)
print('Salário Bruto: ' + salario_bruto)

salario_bruto = float(salario_bruto)
imposto_r = (salario_bruto * 11)/100
imposto_r = str(imposto_r)
print('IR (11%): ' + imposto_r)

salario_bruto = float(salario_bruto)
inss = (salario_bruto * 8)/100
inss = str(inss)
print('INSS (8%): ' + inss)

salario_bruto = float(salario_bruto)
sindicato = (salario_bruto * 5)/100
sindicato = str(sindicato)
print('Sindicato (5%): ' + sindicato)

sindicato = float(sindicato)
inss = float(inss)
imposto_r = float(imposto_r)
salario_bruto =float(salario_bruto)

descontos_totais = imposto_r + inss + sindicato
salario_liquido = salario_bruto - descontos_totais
salario_liquido = str(salario_liquido)
print('Salário Líquido: ' + salario_liquido)

#E8.João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
#o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes 
#maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
#(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa 
#que você faça um programa que leia a variável peso (peso de peixes) e calcule 
#o excesso. Gravar na variável excesso a quantidade de quilos além do limite e 
#na variável multa o valor da multa que João deverá pagar. Imprima os dados do 
#programa com as mensagens adequadas.
peso_limite = 50
multa_por_kg = 4

peso_peixes = (float(input('Peso total: ')))
peso_excedido = peso_peixes - peso_limite
print(f'O peso excedido é: {peso_excedido:.2f}')
multa_em_real = peso_excedido * multa_por_kg
print(f'A multa a ser paga é no valor de: R$ {multa_em_real:.2f}')
