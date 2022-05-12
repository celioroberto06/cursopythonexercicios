media = nota1 = nota2 = 0
dados = []
grupo = []
while True:
    dados.append(str(input('Nome: ')))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    media = (nota1 + nota2) / 2
    dados.append([nota1, nota2])
    dados.append(media)
    grupo.append(dados[:])
    dados.clear()
    if perg in 'N':
        break
print('='*30)
print(f'{"Nº":<8} {"NOME":<10} {"MÉDIA":>10}')
print('-'*30)
for i, n in enumerate(grupo):
    print(f'{i:<8} {n[0]:<10}  {n[2]:>8}')
print('-'*30)
opc = 0
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 para interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(grupo) -1:
        print(f'Notas de {grupo[opc][0]} são {grupo[opc][1]}')


