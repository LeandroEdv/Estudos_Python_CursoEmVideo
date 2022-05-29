velo = int(input('Digite a velocidade: '))
mult = (velo - 80) * 7
if velo > 80:
    print('Você foi multado pois passou {}km do limite, sua multa a de {},00 R$'.format(velo - 80, mult))
else:
    print('tudo ok !')
