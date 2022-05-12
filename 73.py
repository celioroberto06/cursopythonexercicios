times = ('Santos','Atlético - MG','Corinthians', 'Cuiabá',
         'Internacional', 'Avaí', 'Bragantino', 'Palmeiras',
         'Flamengo', 'Coritiba', 'São Paulo', 'Botafogo',
         'Fluminense', 'América-MG', 'Ceará', 'Athletico-PR',
         'Atlético-GO', 'Goiás', 'Juventude ','Fortaleza')
print('-='*45)
print(f'Os 5 primeiros são: {times[:5]}')
print('-='*45)
print(f'Os 4 últimos são: {times[-4:]} ')
print('-='*45)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*45)
print(f'O Corinthians está na {times.index("Corinthians")+1}ª posição')