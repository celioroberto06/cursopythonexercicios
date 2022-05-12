palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRÁTIS', 'ESTUDAR')
for palavra in palavras:
    print(f'\nNa palavra {palavra} aprender temos -> ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')

