r1 = float(input('Primeiro seguimento: '))
r2 = float(input('segundo seguimento: '))
r3 = float(input('terceiro seguimento: '))
tipo = str
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        tipo = str('Equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        tipo = str('isósceles')
    else:
        tipo = str ('escaleno')
    print('Os seguimentos formam um triangulo \033[30;44m{}\033[m !'.format(tipo))

else:
    print('os seguimento não formam um triangulo')