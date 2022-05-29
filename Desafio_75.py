var01 = int(input('Digite o prieiro valor:'))
var02 = int(input('Digite o segundo valor: '))
var03 = int(input('Digite o terceiro valor: '))
var04 = int(input('digite o quarto valor: '))
tupvar = (var01, var02, var03, var04)
print(f'Voçê digitou os numeros {tupvar}')
if 9 in tupvar:
    print(f'o numero 9 apareceu {tupvar.count(9)}')
else:
    print('O numero 9 não apareceu')
if 3 in tupvar:
    print(f'O numero três apareceu na {tupvar.index(3)+1}° posição')
else:
    print('Não foi digitado o numero 3')
print('numeros par: ', end='')
for n in tupvar:
    if n % 2 == 0:
        print(n, end=' ')
