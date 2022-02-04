cor

def ajuda(com):
    help(com)

def título(msg, cor=0):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)
#programa principal
comando = ''
while True:
    título('  SISTEMA DE AJUDA PyHELP  ')
    comando = str(input('Função ou comando > '))
    if comando.upper().strip()== 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!')