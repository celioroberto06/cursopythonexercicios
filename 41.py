from datetime import date
print('-='*10)
print('\033[36mCLASSIFICANDO ATLETA\033[m')
print('-='*10)
ano_nascimento = int(input('Ano de nascimento? '))
idade = date.today().year - ano_nascimento
if idade <= 9:
    print(f'Com {idade} anos você é um atleta MIRIM!')
elif idade <= 14:
    print(f'Com {idade} anos você é um atleta INFANTIL!')
elif idade <= 19:
    print(f'Com {idade} anos você é um atleta JUNIOR!')
elif idade <= 25:
    print(f'Com {idade} anos você é um atleta SêNIOR!')
else:
    print(f'Com {idade} anos você é um atleta MASTER!')