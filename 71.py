print('=' * 18)
print('{:^15}'.format('BANCO CEV'))
print('=' *18)
valor = 0

d = valor // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10



valor = float(input('Que valor você quer sacar? R$'))
total =valor
cédula_atual = 50
tot_cédula = 0
while True:
    if total >= cédula_atual:
        total -= cédula_atual
        tot_cédula += 1
    else:
        if tot_cédula > 0:
            print(f'Total de {tot_cédula} cédulas de R${cédula_atual}')
        if cédula_atual == 50:
            cédula_atual =20
        elif cédula_atual == 20:
            cédula_atual = 10
        elif cédula_atual ==10:
            cédula_atual = 1
        tot_cédula = 0
        if total == 0:
            break
print('='*18)
print('VOLTE SEMPRE')
