import random
print('**** Estou pensando em um numero entre 0 e 10 ****')
tentativas = 0
numberpc = int(random.randint(0, 10))
numberplayer = int(input('digite um numero'))
cont = 0
while numberpc != numberplayer:
    cont += 1
    print('O numero que eu estava pensando era: {}! '.format(numberpc))
    numberplayer = int(input('Digite um numero'))
    numberpc = int(random.randint(1, 10))

print('\033[35mVocê acertou! o numero era {}! Você usou {} tentativas'.format(numberpc, cont))