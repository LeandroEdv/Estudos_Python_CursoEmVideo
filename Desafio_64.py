n = 0
soma = 0
quant = 0
while n != 999:
    n = int(input('digite um numero'))
    if n != 999:
     soma += n
     quant += 1
    else:
        print('foram digitados {} numeros, e a soma dos numeros é {}'.format(quant, soma))