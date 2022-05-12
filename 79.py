valores = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in valores:
        print(f'\033[:31mO valor {valor} já existi na lista! Não vou adicionar...\033[m')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S / N] ')).upper().strip()[0]
    if perg == 'N':
        break
print('='*30)
valores.sort()
print(f'Os valores digitados foram {valores}')