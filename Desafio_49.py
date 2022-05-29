print('Tabuada !')
operation = str(input('Escolha a operação com os sinais: +, -, *, /' ))
number = int(input('Escreva um numero: '))
for n in range(0, 10):
     if operation == '*':
        print('{} X {} = {}'.format(number, n, number * n))
     elif operation == '/':
        print('{} / {} = {}'.format(number, n, number / n))
     elif operation == '+':
        print('{} + {} = {}'.format(number, n, number + n))
     elif operation == '-':
        print('{} - {} = {}'. format(number, n, number - n))
     else:
        print('O oerador não foi encontrado !! ')
        break
