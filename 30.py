
while True:
    numero = int(input('Digite um número qualquer ou [ 999 ] para finalizar: '))
    if numero % 2 == 0:
        print('É PAR')
    elif numero == 999:
        break
    else:
        print('É IMPAR')
print('OBRIGADO POR USAR O PROGRAMA!!!')