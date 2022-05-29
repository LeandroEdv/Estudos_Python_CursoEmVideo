lista = list()
continuar = ' '
contador = 0
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer Continuar [S/N]')).upper()
    if 'N' in continuar:
     break
print(f'Foram digitados: {len(lista)} numeros')
print(f'Os numeos em ordem crescente são: {sorted(lista,reverse=True)}')
if 5 in lista:
    print(f'O numero 5 aparece na lista !')
else:
    print('O numero 5 não aparece!')