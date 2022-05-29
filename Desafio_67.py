print('Tabuada!')
cont = 0
while True:
    print('----'*4)
    n = int(input('Digite um numero '))
    print('----' *4)
    cont = 0
    if n < 0:
        print('Programa Finalizado')
        break
    while cont < 10:
        cont += 1
        print(f'{n} X {cont} = {n * cont}')

