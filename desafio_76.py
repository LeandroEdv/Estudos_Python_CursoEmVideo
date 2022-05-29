lista = ('carne', 35.20, 'leite', 4.50, 'pão', 2.60)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end='')
    else:
        print(f'R${lista[pos]:>3.2f}')