print('-'* 23)
print('\033[:31mCALCULADOR DE DESCONTOS\033[m')
print('-'* 23)
p = float(input('Valor do produto: '))
desc = (p / 100) * 95 # -> p - (p * 5 / 100)

print(f'O produto que custava {p:.2f} com desconto de 5% sae por: {desc:.2f}'.replace('.', ','))