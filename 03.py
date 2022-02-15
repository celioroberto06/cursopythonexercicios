import random
soma = mult = dividir = numero = numero2 = 0

while True:
    numero = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))
    perg = int(input('O que vc quer fazer: 1- Somar '
                     '2- Dividir ' 
                     '3- Multiplicar? '))

    if perg == 1:
        print(f' O resultado é {numero + numero2}')
    elif perg == 2:
        print(f' O resultado é {numero / numero2}')
    else:
        print(f' O resultado é {numero * numero}')
    perg2 = str(input('Quer fazer outra equação? [S / N]  ')).upper().strip()[0]
    if perg2 == 'N':
        break
print('-='*20)
print('Obrigado por utilizar o programa!')