#Tabuada

while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-'*14)
    print('   \033[;31mTABUADA\033[m')
    print('-'*14)
    print(f'{n} x 1 = {n*1}')
    print(f'{n} x 2 = {n*2}')
    print(f'{n} x 3 = {n*3}')
    print(f'{n} x 4 = {n*4}')
    print(f'{n} x 5 = {n*5}')
    print(f'{n} x 6 = {n*6}')
    print(f'{n} x 7 = {n*7}')
    print(f'{n} x 8 = {n*8}')
    print(f'{n} x 9 = {n*9}')
    print(f'{n} x 10 = {n*10}')
    perg = str(input('Quer continuar: [S / N] ')).strip().upper()[0]
    if perg == 'N':
        print('FINALIZANDO TABUADA...')
        break