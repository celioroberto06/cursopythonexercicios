print('-' * 15)
print('LOJA O BARATÃO')
print('-' * 15)
total_compra = mais_caro = mais_barato = nome_barato = 0
perg = cont = 0
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total_compra += preco
    cont += 1
    if preco > 1000:
        mais_caro += 1
    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        nome_barato = nome
    perg  = ' '
    while perg not in 'SN':
        perg = str(input('Quer continuar? [S / N]')).upper().strip()[0]
    if perg == 'N':
        print('-----FIM DO PROGRAMA-----')
        break
print(f'O total da compra foi de {total_compra:.2f}')
print(f'Temos {mais_caro} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R${mais_barato:.2f}')
