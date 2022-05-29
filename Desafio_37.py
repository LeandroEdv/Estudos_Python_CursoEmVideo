number = int(input('Digite um numero '))
baseConv = int(input('Digite 1 para binario 2 para octal e 3 para hexadecimal'))
if baseConv == 1:
    print('O numero em binario é: \033[1;34m{}'.format(bin(number)))
elif baseConv == 2:
    print('o numero em octal é: \033[1;34m{}'.format(oct(number)))
elif baseConv == 3:
    print("o numero convertido para hexadecimal é igual a: \033[1;34m{}".format(hex(number)))
else:
    print('digite uma opção válida' )
