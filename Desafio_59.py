progstatus = True
operation = int(0)
number01 = int(input('Digite o primeiro numero '))
number02 = int(input('Digite o segundo numero '))
while progstatus == True:
    operation = int(input('[1] soma \n[2] multiplicação \n[3] Maior \n[4] Novos numeros \n[5] Sair'))
    if operation == 1:
       print('A soma dos numeros é {}'.format(number01+number02))
    elif operation == 2:
        print('A multipliação é {}'.format(number01 * number02))
    elif operation == 3:
        if number02 > number01:
            print('o maior numero é {} !'.format(number02))
        elif number01 > number02:
            print('o maior numero é {} !'.format(number01))
        else:
            print('Os numeros são iguais !')
    elif operation == 4:
        print('Digite novamente os numeros')
        number01 = int(input('Digite o primeiro numero '))
        number02 = int(input('Digite o segundo numero '))
    else:
        progstatus = False
        print("final do programa")
