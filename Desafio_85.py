lista = [[], []]
valores = 0
for c in range(0, 7):
    valores = (int(input('Digite um valor: ')))
    if valores % 2 == 0:
        lista[0].append(valores)
    else:
        lista[1].append(valores)
print(lista)