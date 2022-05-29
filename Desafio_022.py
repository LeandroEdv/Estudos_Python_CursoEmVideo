
import math
import random
n01 = str(input('Digite Seu nome completo '))
n02 = n01.split()
print(n01.upper())
print(n01.lower())
print('o primeiro nome tem: {} letras'.format(n02[0].__len__()))
print('o nome tem no total {} letras'.format(''.join(n02[:]).__len__()))


