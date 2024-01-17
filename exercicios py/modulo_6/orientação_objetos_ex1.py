#classe -> atibutos ->métodos
#Objeto - Bartolomeu
#Herança - GatoCastrado

from time import sleep
Class Pet (object)
  def __init__ (self, nome:str, sexo:str, cor:str =nome):
    self.nome = nome
    sexo.sexo = sexo
    self.cor = cor
#objeto = gato()
#objeto.atributo
#objeto.metodo()

#método
def dormir(self, horas:int) ->None:
  for hora in range (1, horas + 1):
    print(f'dormindo por {hora} horas')
    sleep (1)
    
#manipulação
#cor_pet =('laranja':'laranja')
#Método __init__: É um método especial chamado de construtor. 
#Ele é automaticamente chamado quando você cria uma nova instância de uma classe. 

#Método __str__: É um método especial que retorna uma representação em string do objeto.
#É chamado automaticamente quando você tenta converter um objeto em uma string, como ao
#imprimir o objeto. 

class Universidade:
  def __init__(self, nome):
    self.nome = nome
class Pessoa:
  def __init__(self, nome, idade, universidade):
    self.nome = nome
    self.idade = idade
    self.universidade = universidade

ufrj = Universidade("UFRJ")
andre = Pessoa("karolina", 23, catolica)
print(karolina.nome) #Vai imprimir "karolina"
print(andre.universidade.nome) #Vai imprimir "UFRJ"
print(andre.universidade) #Vai imprimir algo como 
"<__main__.Universidade object at 0x7f9a7b68b940>"

def __init__(self, nome):
    self.nome = nome
  def __str__(self):
    return f"Universidade: {self.nome}"
print(karolina.universidade) #Vai imprimir "Universidade: UFRJ"

