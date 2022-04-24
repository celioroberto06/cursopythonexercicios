print('=-='*7)
print('\033[31m SUPER GERADOR DE PA\033[m')
print('=-='*7)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
opc = 10
total = 0
while opc != 0:
    total += opc
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('FIM!')
    opc = int(input('\nMais quantos termos você quer que mostre?'))
print(f'O numero de termos mostrados foi {total}')
