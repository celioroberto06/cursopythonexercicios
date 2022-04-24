print('='*12)
print('\033[36mEXERCÍCIO 59\033[m')
print('='*12)
multiplica = soma = n1 = n2 = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = maior = 0
while opc != 5:
    print('')
    print('='*30)
    print('''\033[36m    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] sair do programa\033[m''')
    print('=' * 30)
    opc = int(input('Qual é a sua opção? '))
    print('')
    if opc == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif opc == 2:
        multiplica = n1 * n2
        print(f'{n1} x {n2} = {multiplica}')
    elif opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opc == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor:  '))
    elif opc == 5:
        print('Finalizando o programa!!!')
    else:
        print('Opção inválida tente novamente!')
