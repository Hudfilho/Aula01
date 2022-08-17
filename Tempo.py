def calcula_minutos():
  minutos = float(input('Informe a quantidade de minutos '))
  horas = float(input('Informe o numero de horas '))
  dias = float(input('Informe o numero de dias '))
  minutos_totais = (dias*24*60+horas*60+minutos)
  
  print(minutos_totais, ' minutos')

def calcula_segundos():
  minutos = float(input('Informe a quantidade de minutos '))
  horas = float(input('Informe o numero de horas '))
  dias = float(input('Informe o numero de dias '))
  segundos_totais = 60*(dias*24*60+horas*60+minutos)

  print(segundos_totais, ' segundos')