from math import hypot
print('-'* 28)
print('\033[:31mCALCULANDO A HIPOTENUZA\033[m')
print('-'* 28)
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenuza vai medir {hypot(co, ca):.2f}')