print('-CALCULADOR DE CUSTO DE VIAGEM-')
print('-='*15)
distancia = float(input('Digite a distância da viagem em km: '))
if distancia <= 200:
    valor1 = distancia * 0.50
    print(f'O valor da sua passagem até 200km será {valor1:.2f} ')
if distancia > 200:
    valor2 = distancia * 0.45
    print(f'O valor da sua passagem acima de 200km será {valor2:.2f}')
print('')
print('BOA VIAGEM')