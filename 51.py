print('='*19)
print('\033[31m10 TERMOS DE UMA PA\033[m')
print('='*19)
inicio = razao =0
inicio = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = inicio +(10 - 1) * razao
for c in range(inicio, decimo + razao, razao):
    print(f'{c} -> ', end='')
print('ACABOU')