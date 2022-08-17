def __init__(self,name):
      self.name = name

def calcula_distancia():
  
  kmPorLitro = float(input('Informe quantos quilometros o carro percorre com um litro '))
  gasolina = float(input('Informe a quantidade de gasolina armazenada '))
  
  kmRodados = kmPorLitro*gasolina
  print(kmRodados, ' Km percorridos')