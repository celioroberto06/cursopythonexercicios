from datetime import date

print('-='*15)
print('Digite o ano para analizar ou 0 para o ano atual')
print('-='*15)
ano = int(input('Digite o ano para saber se é bissexto: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é BISSEXTO.')
else:
    print(f'{ano} não é BISSEXTO.')