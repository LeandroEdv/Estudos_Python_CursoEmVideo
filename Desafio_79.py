lista = []
continuar = ' '
novovar = 0
while True:
    novovar = int(input('Digite o valor: '))
    if novovar not in lista:
        lista.append(novovar)
    else:
        print('o valor já existe na lista!')
    continuar = input('quer continuar ? [S/N]').upper()
    if continuar == 'N':
        break
print(f'os valores em ordem crescente são: {sorted(lista)}')
