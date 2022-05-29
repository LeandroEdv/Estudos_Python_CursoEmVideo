valorCasa = int(input('Digite o valor da casa: '))
salario = int(input( 'Digite o seu salario: '))
anos = int(input('Digite quantas anos para pagar: '))
anos = anos * 12
maxcusto = (30 * salario) / 100
valorparcelas = valorCasa / anos

if maxcusto >= valorparcelas:
    print("Voce pode comprar a casa !! \n as parcelas são de: {:.2f}".format(valorparcelas))
else:
    print ('voce não podera comprar ! 30% do seu salaro é {:.2f} e as parcelas são: {:.2f}'.format(maxcusto, valorparcelas))