import random

n01 = str(input('Escreva um numero de 0 á 5: '))
n02 = str(random.randint(0, 5))
print('O numero que estava pensando era {} !'.format(n02))
if n01 == n02:
    print('Você acertou !')
else:
    print('Você Errou !')

