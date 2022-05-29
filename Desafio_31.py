numkilo = int(input('Quantos Km´s será sua viajem ? '))
if numkilo >= 200:
  result = numkilo * 0.50
  print('sua viajem de \033[1;30;44m {}Km´s \033[m custara {}'.format(numkilo, result))
else:
  result = numkilo * 0.45
  print('sua viajem de {}Km´s custara \033[0;32m {}'.format(numkilo, result))
