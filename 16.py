from math import floor, trunc
print('-'* 28)
print('\033[:31mPORÇÃO DE UM NÚMERO INTEIRO\033[m')
print('-'* 28)
n = float(input('Digite um número: '))
print(f'O valor digitado foi {n} e sua porção inteira é {trunc(n)}')