numeros = []
perg = ''
while True:
    numeros.append(int(input('Digite um valor: ')))
    perg = str(input('Quer continuar? [S / N]')).upper()[0].strip()
    if perg in 'N':
        break
numeros.sort(reverse=True)
print(f'Você digitou {len(numeros)} elementos.')
print(f'Os valores digitados em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontardo na lista!')