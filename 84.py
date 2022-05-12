pesado = leve = nome_pesado = nome_leve = cont = 0
dados = list()
academia = list()
while True:
    academia.append(str(input('Nome: ')))
    academia.append(float(input('Peso: ')))
    if len(dados) == 0:
        pesado = leve = academia[1]
    else:
        if academia[1] > pesado:
            pesado = academia[1]
        if academia[1] < leve:
            leve = academia[1]

    dados.append(academia[:])
    academia.clear()
    perg = str(input('Quer continuar? ')).upper()[0]
    if perg in 'N':
        break
print('='*30)
print(f'Ao todo foram cadastradas {len(dados)} pessoas')
for p in dados:
    if p[1] == pesado:
        print(f'[{p[0]}] ',end='')
print(f' tem o maior peso {pesado}kg')
for p in dados:
    if p[1] == leve:
        print(f'[{p[0]}] ', end='')
print(f' tem o menor peso {leve}kg')