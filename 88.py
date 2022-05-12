from random import randint
from time import sleep
lista = []
jogos = []
tot =  1
print('-'*30)
print('      JOGO NA MEGA SENA')
print('-'*30)
quant = int(input('QUANTOS JOGOS VOCÊ QUER QUE EU SORTEIE? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=-=-= SORTEANDO {quant} JOGOS =-=-=-')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('='*5,' BOA SORTE ','='*5)
