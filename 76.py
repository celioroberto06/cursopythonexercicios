print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*30)
produtos = ('lápis',1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.90,
            'Trasferidor', 4.20, 'Compasso', 9.99,'Mochila',120.00, 'Canetas', 22.30,
            'Livro', 34.90)
print()
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-'*39)