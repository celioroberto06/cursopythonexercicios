import random
numero = 0
print('-='*10)
print('ADIVINHANDO O NÚEMRO')
print('-='*10)
pergunta = int(input('Tente acertar o número que estou pensando de 1 a 5: '))
numero = (random.randint(1, 6))
if pergunta == numero:
    print(f'PARABÉNS eu pensei no número {numero}.')
else:
    print(f'ERROU! Eu pensei no número {numero}')