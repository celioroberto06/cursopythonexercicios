while True:
    def escreva(msg):
        tam = len(msg)+4
        print('=' * tam)
        print(f'  {msg}')
        print('=' * tam)
    msg = str(input('Digite um nome: '))
    escreva(f'{msg}')
    perg = ''
    perg = str(input('Quer continuar [S / N]')).strip().upper()[0]
    if perg == 'N':
        break
