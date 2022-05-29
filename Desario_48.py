print('soma numeros multiplos de 3, de 1 a 500')
s = 0
for n in range(1, 501):
    if n % 3 == 0:
        s += n
print('vez \033[35m{}\033[m soma: {}'.format(n, s), end=' ')
