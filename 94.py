media_geral = total = media = 0
dados_gerais = []
pessoas = {}
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    while True:
        pessoas['Sexo'] = str(input('Sexo: [M / F]')).strip().upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['Idade'] = int(input('Idade: '))
    media += pessoas['Idade']
    dados_gerais.append(pessoas.copy())

    while True:
        perg = str(input('Quer continuar? [S / N] ')).upper().strip()[0]
        if perg in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if perg == 'N':
        break

media_geral = media / len(dados_gerais)
print('='*35)
print(f'A) Ao todo foram {len(dados_gerais)} cadastradas')
print(f'B) A média geral foi de {media_geral:.2f}')
print(f'C) As mulheres cadastradas foram ',end='')
for p in dados_gerais:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}, ', end='')
print()
print('C) Lista de pessoas que estão acima da média: ')
for p in dados_gerais:
    if p['Idade'] >= media_geral:
        print(f'{p["Nome"]} com {p["Idade"]}')
