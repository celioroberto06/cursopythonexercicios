media = 0
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input('Média: '))
if dados['média'] < 5:
    dados['situação'] = 'REPROVADO'
else:
    if 5 <= dados['média'] < 7:
        dados['Situação'] = 'RECUPERAÇÃO'

    elif dados['média'] >= 7:
        dados['Situação'] = 'APROVADO'
for k, v in dados.items():
    print(f'- {k} é igual a {v}')