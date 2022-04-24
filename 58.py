import random
print('='*19)
print('\033[36mADIVINHANDO NúMEROS\033[m')
print('='*19)
numero = palpite = 0
print('''Olá eu sou seu computador e estou
pensando em um número entre 0 À 10 tenta adivinhar.''')
numero = (random.randint(1, 11))
pergunta = int(input('Qual é o seu palpite? : '))
while pergunta != numero:
    if pergunta < numero:
        print('mais...',end=' ')
    elif pergunta > numero:
        print('Menos...',end=' ')
    pergunta = int(input('Errou, qual é o seu palpite? : '))
    palpite += 1
print(f'Parabéns acertou eu pensei no número {numero}')
print(f'Você errou {palpite} vezes')