from datetime import date
dados = {}
ano_atual = date.today().year
dados['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual - ano_nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['ano_contrato'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano_contrato'] + 35) - ano_atual)
print('-='*20)
print(dados)
for i, v in dados.items():
    print(f'- {i} tem o valor {v}')