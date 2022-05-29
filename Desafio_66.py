soma = media = cont = 0
while True:
    nu = int(input('Digite um numero (999 para parar !)'))
    if nu == 999:
        break
    cont += 1
    soma += nu
media = soma / cont
print(f'foram digitados {cont} a soma dos numeros é {soma}, a média é {media}')