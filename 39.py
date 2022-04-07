print('-='*10)
print('\033[31mALISTAMENTO MILITAR\033[m')
print('-='*10)

from datetime import date
nasc = int(input('Ano de nascimento: '))
data_atual = date.today().year
idade_atual = data_atual - nasc
anos_atrasado = idade_atual -18
menor_idade = 18 - idade_atual
if idade_atual > 18:
    print(f'Você esta com {idade_atual} anos e já passou {anos_atrasado} anos do tempo.')
if idade_atual == 18:
    print(f'Você tem {idade_atual} anos e tem que se alistar esse ano!')
if idade_atual < 18:
    print(f'Você está com {idade_atual} anos e ainda faltam {menor_idade} anos para se alistar.')