def aumentar(preço=0, taxa=0, formato=False):
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