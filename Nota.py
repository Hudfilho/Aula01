def calcula_nota():
  Ap1 = float(input('Informe a nota da Ap1 '))
  Ap2 = float(input('Informe a nota da Ap2 '))
  Ac = float(input('Informe a nota da Ac '))
  media = (Ap1*0.4+Ap2*0.4+Ac*0.2)
  print(media)
  if media>=7:
    print('Aprovado')
  else:
    print('Reprovado')