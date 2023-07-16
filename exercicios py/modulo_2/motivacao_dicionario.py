#para se conectar a uma rede wi-fi, você precisa de duas informações: o nome da rede
#e a senha de acesso. quando você vai acessar uma nova rede, você encontra uma lista
#de redes disponíveis:

wifi_disponiveis = ['mob300', '40028922', 'aespa_link', '_net']
print(wifi_disponiveis)

#você consegue identificar quais são os nomes de redes e suas respectivas senhas?
#talvez uma list não seja a melhor opção para armazenar esse tipo de dado. 
#resolução:

wifi_disponiveis = []
rede = {'nome':'mob300', 'senha': '40028922'}
wifi_disponiveis.append(rede)
rede = {'nome': 'aespa_link', 'senha':'_net'}
wifi_disponiveis.append(rede)
print(wifi_disponiveis)
