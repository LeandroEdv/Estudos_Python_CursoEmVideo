times = ('América FC SAF - MG', 'Atlético - GO','Atlético Mineiro - MG', 'Atlético Mineiro - MG',
'Avaí - SC', 'Botafogo - RJ','Ceará - CE','Corinthians - SP','Coritiba - PR','Flamengo - RJ', 'Fluminense - RJ',
'Fortaleza - CE', 'Goiás - GO', 'Internacional - RS', 'Juventude - RS','Palmeiras - SP', 'Red Bull Bragantino - SP'
'Santos - SP', 'São Paulo - SP')
pos = 0
print(f'Os primeiros 5 times são:{times[0:5]}')
print(f'os 4 ultimos times são: {times[-3:]}')
print(f'os times em ordem alfabetica são: {sorted(times)}')
pos = times.index('Internacional - RS')
print(f'o time esta Internacional - RS está na posição: {pos}')