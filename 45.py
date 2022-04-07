from random import randint
while True:
    lista_pc = ('PEDRA','PAPEL','TESOURA')
    jogada_pc = randint(0, 2)

    print('-='*5)
    print('\033[36mJO KEM PO\033[m')
    print('-='*5)
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    opc = int(input('Qual é sua jogada ou 999 para sair? '))


    print('\033[1;31m-=\033[m'*15)
    print(f'O computador jogou {lista_pc[jogada_pc]}')
    if opc == jogada_pc:
        print('EMPATE')
    elif opc == 0 and jogada_pc == 2:
        print('Você ganhou!')
    elif opc == 1 and jogada_pc == 0:
        print('Você ganhou!')
    elif opc == 2 and jogada_pc == 1:
        print('Você ganhou!')
    elif opc == 999:
        break
    else:
        print('Computador ganhou!')
    print('\033[1;31m-=\033[m'*15)
