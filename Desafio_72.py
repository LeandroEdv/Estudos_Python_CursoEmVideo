numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez')
n = -1
while n > 10 or n < 0:
    n = int(input('digite um numero entre 0 e 10 '))
    if n > 10 or n <0:
        print('tente novamente')
print(f'o numero digitado foi: {numeros[n]}')