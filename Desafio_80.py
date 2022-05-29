valores =[]
var = 0
pos = 0
maior = 0
menor = 0
posmaior = 0
pormenor = 0
for i in range(0, 5):
    var = input('digite um valor')
    if i == 0:
        maior = var
        menor = var
        #valores.insert(0, var)
        valores.append(var)
        print('primeira posição')
    if var > valores[-1]:
        maior = var
        posmaior = 0
       # valores.insert(posmaior, maior)
        valores.append(var)
        print('pos fim da lista')
    if var < menor:
        menor = var
        valores.insert(0, var)
        print ('')
    if var > menor and var < maior:

        valores.insert(1, var)

print(valores)
