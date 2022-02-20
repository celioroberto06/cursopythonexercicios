#converso de moeda REAL X DOLAR
real = float(input('Quanto de dinheiro você tem na carteira: '))
dolar = real / 5.14
print(f'Com {real} você consegue comprar {dolar:.2f} de dólar'.replace('.', ','))