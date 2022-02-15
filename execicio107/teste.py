import moedas
from time import sleep

p = float(input('Digite um preço: R$ '))
print('Calculando...')
sleep(2)
print(f'A metade de {p} é {moedas.metade(p)}')
sleep(1)
print(f'O dobro de {p} é {moedas.dobro(p)}')
sleep(1)
print(f'Aumentando 10 % de {p} é {moedas.aumentar(p, 10)}')

