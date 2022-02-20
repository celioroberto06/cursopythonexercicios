print('-'* 30)
print('\033[:31mCALCULADOR AUMENTO DE SALÁRIO\033[m')
print('-'* 30)
salario = float(input('Qual o salário? '))
aumento = salario + (salario * 15 / 100)
print(f'O funcionário que recebia {salario:.2f} com 15% de aumento\n'
      f'agora vai receber {aumento:.2f}')