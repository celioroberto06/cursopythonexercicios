from execicio109 import moedas
from time import sleep

p = float(input('Digite um preço: R$ '))
print('Calculando...')
sleep(2)
print(f'A metade de {moedas.moedas(p)} é {moedas.metade(p, True)}')
sleep(1)
print(f'O dobro de {p} é {moedas.dobro(p, True)}')
sleep(1)
print(f'Aumentando 10 % temos {moedas.aumentar(p, 10, True)}')
sleep(1)
print(f'Diminuir 20 % temos {moedas.diminuir(p, 20, True)}')