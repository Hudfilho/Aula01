class Area():

  def __init__(self,name):
    print("Uma area foi chamada")   
    self.name = name

class Quadrado(Area):
  def __init__(self, name):
    print("Um quadrado foi criado!")
    self.name = name
  
  def area(lado):
    lado = float(input('Informe o tamanho do lado '))
    print(lado*lado, 'm')

class Retangulo(Area):
  def __init__(self, name):
    print("Um retangulo foi criado!")
    self.name = name
  
  def area(self):
    altura = float(input('Informe a altura '))
    largura = float(input('Informe a largura '))
    print(altura*largura, 'm')
