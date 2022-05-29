n = int(input('Digite um numero '))
cont = n
result = 1
while cont > 1:
    result = result * cont
    cont -= 1
    n -= 1
    print(cont, result)