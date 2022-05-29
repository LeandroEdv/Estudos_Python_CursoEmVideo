dados = list()
lista = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso')))
    lista.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar ? [S/N]')).upper()
    if 'N' in continuar:
        break
print(f'foram cadastradas {len(lista)} pessoas')
for c in range(0, len(lista)):
    if lista[c][1] >= 100:
        print(f'{lista[c][0]} tem mais de 100kg')
    elif lista[c][1] <= 70:
        print(f'{lista[c][0]} tem menos que 70Kg')


print(f'')