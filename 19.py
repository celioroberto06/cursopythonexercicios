from random import choices
nome =[]

cont = 0
for c in range(4):
    cont += 1
    nome.append(str(input(f'Digite {cont}º nome: ')))
escolha = choices(nome)
print(f'O nome escolhido foi: {escolha}')
