def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

#programa principal
n = str(input('Digite o nome do jogador: '))
g = str(input('Quantos gols no campeonato: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
