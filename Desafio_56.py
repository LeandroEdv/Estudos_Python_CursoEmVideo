somaidade = 0
mediaidade = 0
maioridadehomen = 0
idade = 0
nomehomen = ''
for p in range (1, 5):
    print('*---- {}ª pessoa ----*'.format(p))
    nome = str(input('Digite o nome '))
    idade = int(input('Digite a idade '))
    sexo = str(input('sexo M/F'))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
     maioridadehomen = idade
     nomehomen = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomehomen = nome
mediaidade = somaidade / 4
print('A média das idades é {} O Homen mais velho é {} e tem {} anos'.format(mediaidade, nomehomen, maioridadehomen))
