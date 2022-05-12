from random import randint
from operator import itemgetter
rankin = {}
jogadores = {'Jogador-1':randint(1, 6), 'Jogador-2':randint(1, 6),
             'Jogador-3':randint(1, 6), 'Jogador-4':randint(1, 6)}
print('VALORES SORTEADOS')
for i, v in jogadores.items():
    print(f'{i} tirou {v} no dado')
print('='*29)

rankin = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('  ==RANKING DOS JOGADORES==')
for i, v in enumerate(rankin):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')