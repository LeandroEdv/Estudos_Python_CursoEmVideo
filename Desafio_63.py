n = int(input('Quantidade de numero sa sequência'))
fn = 0
n01 = 0
n02 = 1
cont = 0
while cont < n:
    print('{}'.format(fn), end=" ")
    fn = n01 + n02
    n01 = n02
    n02 = fn
    cont +=1