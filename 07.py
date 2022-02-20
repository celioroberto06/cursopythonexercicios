# média aritimética
def linha(msg):
    print('-'*35)
    print(msg)
    print('-'*35)


linha('         Média Aritimética')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

linha(f'A média aritmética do aluno é {m:.1f}')