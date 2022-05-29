lista = []
listaPar = []
listaimpar = []
elemento = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = input('quer continuar ?').upper()
    if 'N' in continuar:
        break
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        listaPar.append(lista[c])
    else:
        listaimpar.append(lista[c])

print(f'todos os elementos são: {lista}')
print(f'os numeros par são: {listaPar}')
print(f'os numeros impar são {listaimpar}')