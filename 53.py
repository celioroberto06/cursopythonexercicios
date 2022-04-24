print('='*19)
print('\033[33mDETECTOR DE PALíNDROMO\033[m')
print('='*19)
frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
palavras = frase.split()
junto = ' '.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print(f'O inverso de {junto} é {inverso} e forma um Palíndromo!')
else:
    print(f'O inverso de {frase} é {frase[::-1]} e NÃO forma um Palíndromo!')
