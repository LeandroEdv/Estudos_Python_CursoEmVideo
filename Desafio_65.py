soma = 0
media = 0
cont = 0
maior = 0
menor = 0
continuar = 'S'
while continuar in 'Ss':
    n = int(input('Digite um valor'))
    soma += n
    cont += 1
    menor = n
    if maior < n:
        maior = n
    if n < menor:
      menor = n
    continuar = str(input('Quer continuar ? [S/N]')).upper()
    if continuar == 'N':
        print(' a media foi {}, o maior numero foi {} o menor numero foi:{}'.format(soma/cont, maior, menor))