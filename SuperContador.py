
contSexo = 0
contIdade = 0
contLoira = 0
while True:
    sexo = str(input('Sexo: '))
    idade = int(input('Idade: '))
    print('Cor do cabelo')
    op = int(input('1 - Preto\n2 - Ruivo\n3 - Loiro\n'))
    resp = str(input('Quer continuar? '))
    if sexo == 'f':
        contSexo = contSexo + 1
    if idade >= 18:
        contIdade = contIdade + 1
    if op == 3:
        contLoira = contLoira + 1
    if resp == 'n':
        break
print(f'Quantidade de loiras {contLoira}, de {contSexo}, {contIdade}')