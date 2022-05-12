print('=' * 18)
print('{:^15}'.format('Número por extenso'))
print('=' *18)
numeros = ('zero', 'um', 'dois','três','quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dessoito', 'dezenove','vinte')

while True:
    opc = int(input('Digite um número ente 0 e 20: '))
    if 0 <= opc <= 20:
        break
    print('Tente npvamente')
print(f'Você digitou o número {numeros[opc]}')