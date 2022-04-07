print('-='*11)
print('\033[36m-----LOJAS SANTOS-----\033[m')
print('-='*11)

preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x No cartão
[ 4 ] 3x Ou mais no cartão
''')
opc = int(input('Digite a opção? '))
if opc == 1:
    desconto_10 = preco - (10 / 100 * preco)
    print(f'Valor final com desconto de 10% R$ {desconto_10:.2f}')
elif opc == 2:
    desconto_5 = preco - (5 / 100 * preco)
    print(f'Valor final com desconto de 5% R$ {desconto_5:.2f}')
elif opc == 3:
    parcela = preco / 2
    print(f'Em 2x a parcela fica R$ {parcela:.2f}')
else:
    parcela = int(input('Quantas parcelas? '))
    acresc_20 = preco + (20 / 100 * preco)
    parcelado = acresc_20 / parcela
    print(f'Sua compra será parcelada em {parcela}X de R${parcelado:.2f} com juros')
    print(f'A compra de R${preco:.2f} vai custar R${acresc_20:.2f}')