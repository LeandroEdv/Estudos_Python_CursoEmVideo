matriz = [[[], [], []], [[], [], []], [[], [], []]]
for c in range(0, len(matriz)):
    matriz[0][c].append(int(input(f'digite o valor para: [0, {c}]')))
for c in range(0, 3):
    matriz[1][c].append(int(input(f'digite o valor para: [1, {c}]')))
for c in range(0, 3):
    matriz[2][c].append(int(input(f'digite o valor para: [2, {c}]')))

print(matriz[0])
print(matriz[1])
print(matriz[2])