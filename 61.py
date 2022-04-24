print('='*19)
print('\033[31m10 TERMOS DE UMA PA PT2\033[m')
print('='*19)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('ACABOU')