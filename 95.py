time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} fez? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols no {c+1}º jogo: ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        perg = str(input('Quer continuar? [S / N]')).strip().upper()
        if perg in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if perg == 'N':
        break

print('='*35)
print(f'COD',end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for i, v in enumerate(time):
    print(f'{i:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*35)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse código {busca}')
        print()
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No {i+1}º jogo fez {g} gols.')
    print('-'*35)
print('<<< VOLTE SEMPRE >>>')