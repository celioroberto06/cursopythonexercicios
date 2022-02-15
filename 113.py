def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[41mERRO! Digite um número real:\033[m ')
        except (KeyboardInterrupt):
            print('\033[41mUsúario preferiu não digitar esse número.\033[m ')
            return 0
        else:
            return n

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real:')
print(f'O número inteiro digitado foi {n1} e o real {n2}')