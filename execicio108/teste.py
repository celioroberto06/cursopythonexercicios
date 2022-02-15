import moedas
from time import sleep

p = float(input('Digite um preço: R$ '))
print('Calculando...')
sleep(2)
print(f'A metade de {moedas.moedas(p)} é {moedas.moedas(moedas.metade(p))}')
sleep(1)
print(f'O dobro de {p} é {moedas.moedas(moedas.dobro(p))}')
sleep(1)
print(f'Aumentando 10 % temos {moedas.moedas(moedas.aumentar(p,10))}')

