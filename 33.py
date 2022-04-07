'''numeros = []
cont=0
for c in range(3):
    numeros.append(int(input(f'{c+1}º valor: ')))
    cont += 1'''

nMaior = nMenor = 0
n1 = int(input('1º Valor: '))
n2 = int(input('2º valor: '))
n3 = int(input('3º Valor: '))
nMaior = n1
if n2 > n1 and n3:
    nMaior = n2
if n3 > n1 and n2:
    nMaior = n3
nMenor = n1
if n2 < n1 and n3:
    nMenor = n2
if n3 < n1 and n2:
    nMenor = n3
else:
    print('\033[;31mTODOS SÃO IGUAIS\033[m')
print(f'\033[1;32mO maior número é: {nMaior}\033[m')
print(f'\033[1;35mO menor numero é: {nMenor}\033[m')