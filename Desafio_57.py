s = str(input('Digite seu sexo')).strip().upper()[0]
while s != 'M' and s != 'F':
    print('dados invalidos')
    s = str(input('Digite novamente seu sexo')).strip().upper()[0]
print('Sexo registrado')