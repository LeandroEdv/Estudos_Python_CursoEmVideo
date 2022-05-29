valor = int(input('Digite quanto deseja sacar: '))
contador = 0
cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas01 = 0
while valor > 0:
    while valor != 0 and valor % 50 > 50:
        cedulas50 += 1
        valor -= 50
    while valor != 0 and valor % 20 == 0:
        cedulas20 += 1
        valor -= 20
    while valor != 0 and valor % 10 == 0:
        cedulas10 += 1
        valor -= 10
    while valor != 0 and valor % 1 == 0:
        valor -= 1

print(cedulas50, cedulas20, cedulas10, cedulas01)
