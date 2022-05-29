sexo = ' '
idade = ''
proximo = ' '
pessoa18 = 0
homens = 0
mulheres20 = 0
while True:
    #while sexo != 'M' and sexo != 'F':
       # sexo = str(input('sexo: [M/F]')).upper()
    while proximo not in 'sSNn':
        proximo = str(input('Quer continuar ? [S/N]'))
    idade = int(input('Digite a idade: '))
print(f'pessoas com mais de 18 anos: {pessoa18} homens: {homens} mulheres com menos de 20 anos: {mulheres20}')
