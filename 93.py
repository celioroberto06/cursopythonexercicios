total_gols = 0
dados_jogos = {}
gols = []
dados_jogos['Nome'] = str(input('Nome do jogador: '))
dados_jogos['Partidas'] = int(input(f'Quantas partidas {dados_jogos["Nome"]} fez? '))

for c in range(0, dados_jogos["Partidas"]):
    gols.append(int(input(f'Quantos gols no {c+1}º jogo: ')))
    total_gols += gols[c]
dados_jogos['Gols'] = gols[:]
dados_jogos['Total de gols'] = total_gols

print('='*35)

print(dados_jogos)
print('='*35)
for i, v in dados_jogos.items():
    print(f'O campo {i} tem o valor {v}')

print('=' * 35)

print(f'O jogador {dados_jogos["Nome"]} fez {dados_jogos["Partidas"]} partidas.')
for i, v in enumerate(dados_jogos['Gols']):
    print(f'  => Na {i+1}º Fez {v} Gols ')
print(f'Foi um total de {dados_jogos["Total de gols"]} gols')
