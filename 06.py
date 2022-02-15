from time import sleep
def leiavalor(msg):
    válido = False
    while not válido:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n.strip() == '':
            print(f'\033[0:31mERRO: \"{n}\" é um número inválido!\033[m')
        else:
            válido = True
            return float(n)


n = leiavalor('Digite um número: ')
d = n * 2
t = n * 3
r = n ** (1/2)
print('-'*30)
print('\033[0:31mANALIZANDO O VALOR\033[m'.center(40))
print('-'*30)
sleep(1)
print(f'O dobro de {n} é:    \t{d:.2f}')
print(f'O trilpo  de {n} é:   \t{t:.2f}')
print(f'A raiz quadrada de {n:.0f} é: {r:.0f}')