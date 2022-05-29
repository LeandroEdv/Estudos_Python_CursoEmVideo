var01 = list()
maior = 0
posmaior = 0
menor = 0
posmenor = 0
conta = 0
for c in range(0, 5):
    var01.append(int(input('Digite um numero: ')))
print(f'alista de numeros é: {var01}')
for c, v in enumerate(var01):
    conta += 1
    if v >= maior:
        maior = v
        posmaior = c
    if conta == 1:
        menor = v
    if v <= menor:
        menor = v
        posmenor = c

print(f'O maior numero foi {maior} na posição {posmaior}')
print(f'O menor numero foi {menor} na posição {posmenor}')