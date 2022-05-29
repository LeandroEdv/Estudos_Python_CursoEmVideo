n = int(input('Digite o valor '))
r = int(input('Digite a rasão '))
pa = n
cont = 0
t = 10
while t != 0:
    while cont < t:
        pa = (pa + r)
        cont +=1
        print('{} '.format(pa), end='')

    t = int(input('\ndigite novos termos'))
    cont = 0
