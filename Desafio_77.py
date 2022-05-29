palavras = ('não', 'sei', 'escrever', 'vou', 'tentar', 'mais', 'uma', 'vez')
for p in palavras:
    print(f'A palavra: {p}')
    for letra in p:
        if letra in 'aeiou':
         print(letra, end=' ')