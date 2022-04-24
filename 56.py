print('='*21)
print('\033[36mANALIZADOR DE PESSOAS\033[m')
print('='*21)
media = novo = nome_velho = nome_homemNovo = maior_idade = mulher20 = tot_idade = 0
for dados in range(1, 4):
    print(f'\n----- {dados}ª PESSOA -----')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade : '))
    sexo = str(input(f'Sexo [F / M]: ')).upper().strip()[0]
    tot_idade += idade
    if dados == 1:
        maior_idade = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1
media = tot_idade / 2
print(f'A média de idade das 4 pessoas é: {media}')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos. ')
print(f'O homem mais velho do grupo tem {maior_idade} anos e se chama {nome_velho}')