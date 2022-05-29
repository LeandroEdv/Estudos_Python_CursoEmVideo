from random import randint
escolha = ''
n = 0
cpun = 0
soma = 0
acertos = 0
while True:
     n = int(input('Digite um numero: '))
     escolha = str(input('Par ou Ímpar[P/I]')).upper()
     cpun = randint(0, 100)
     soma = n + cpun
     if soma % 2 == 0:
      print(f'Par! você jogou {n} e o Cpu {cpun} ! a soma é {soma}')
      if escolha in 'Pp':
           acertos += 1
      else:
           break
     if soma % 2 != 0:
          print(f'Ínpar! você jogou {n} e o Cpu {cpun} ! a soma é {soma}')
          if escolha in 'Ii':
               acertos += 1
          else:
             break
print(f'numero de acertos consecutivos = {acertos}')