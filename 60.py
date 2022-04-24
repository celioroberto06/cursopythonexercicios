print('='*12)
print('\033[36mCALCULANDO O FATORIAL\033[m')
print('='*12)
fatorial = 0
num = int(input('Digite um número para ver seu fatorial: '))
c = num
f = 1
print(f'Calculando o fatorial de {num}! = ',end='')
while c > 0:
    print(f'{c} ', end='' )
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')