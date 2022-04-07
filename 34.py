aumento = 0


salario = float(input('Digite o sálario atual R$: '))
if salario >= 1250.00:
    aumento = salario + (salario/100 * 10)
    print(f'Com aumento de 10% voprint('-='*15)
print('\033[1;31mCALCULADOR DE AUMENTO SALáRIAL\033[m')
print('-='*15)cê passa a receber \033[1;31m{aumento:.2f}\033[m')
else:
    aumento = salario + (salario / 100 * 15)
    print(f'Com aumneto de 15% você passa a receber \033[1;31m{aumento:.2f}\033[m')