nomebarato = ' '
precobarato = 0
total = 0
maisdemil = 0
while True:
    cont = ' '
    pn = str(input('Digite o nome do produto: '))
    pc = int(input('Digite o preço do produto: '))
    total += pc
    if precobarato == 0:
        precobarato = pc
        nomebarato = pn
    if pc < precobarato:
        precobarato = pc
        nomebarato = pn
    if pc > 1000:
        maisdemil += 1
    while cont not in 'SN':
        cont = str(input('Quer continuar ? [S/N]')).upper()[0]
    if cont in 'N':
        break
    else:
            print('continuando a cadastrar !')
print(f'o total foi de {total}, O produto mais barato foi {nomebarato} e custou {precobarato}.\n{maisdemil} produtos passaram de mil reais')