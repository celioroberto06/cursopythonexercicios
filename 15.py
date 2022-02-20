print('-'* 16)
print('\033[:31mALUGUEL DE CARRO\033[m')
print('-'* 16)
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos KM rodados? '))
total = dias * 60 + km * 0.15
print(f'Valor total a ser pago {total:.2f}'.replace('.', ','))