numeros = []
pares = []
impares = []
perg = ''
'''while True:
    valor = int(input('Digite um número: '))
    numeros.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    perg = str(input('Quer continuar? [S / N] '))[0].strip().upper()
    if perg in 'Nn':
        break
print('='*30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')'''

# opção 2:

while True:
    numeros.append(int(input('Digite um valor: ')))
    perg = str(input('Quer continuar? [S / N] ')).strip()[0]
    if perg in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('='*30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')