def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 13<= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return  f'Com {idade} anos: VOTO OBRIGATÓRIO!'


nome = str(input('Qual é seu nome? '))
nasc = int(input('Em que ano você nasceu? '))
print(nome)
print(voto(nasc))
