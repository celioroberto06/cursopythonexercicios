from time import sleep
def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Calcula um determinado preço, retornando um
    resultado com ou sem formatação.
    :param preço: O preço que se quer reajustar
    :param taxa: Qual a porcentagem do aumento
    :param formato: Quer a saída formatada ou não?
    :return: O valor reajustado, com ou sem formato.
    '''
    res = preço + (preço * taxa / 100)
    return res if formato is False else moedas(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moedas(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moedas(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moedas(res)

def moedas(preço=0, moedas='R$'):
    return f'{moedas}{preço:>.2f}'.replace('.', ',')

def resumo(preço=0, taxa1=10, taxa2=5 ):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analizando: {moedas(preço)}\n')
    sleep(1)
    print(f'O dobro de é: \t\t{dobro(preço, True)}')
    print(f'A metade é: \t\t{metade(preço, True)}')
    print(f'{taxa1} de aumento: \t\t{aumentar(preço,taxa1, True)}')
    print(f'{taxa2} a menos: \t\t{diminuir(preço, taxa2, True)}')
    print('-'*30)
