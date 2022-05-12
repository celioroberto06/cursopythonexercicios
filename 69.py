print('-'*22)
print('CADASTRO DE PESSOAS')
print('-'*22)

quant_idade = quant_homem = mulher_menorDe20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M / F] ')).upper().strip()[0]
    print('-' * 22)
    if idade > 18:
        quant_idade += 1
    if sexo == 'M':
        quant_homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menorDe20 +=1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar: [S / N]')).upper().strip()[0]
    if pergunta == 'N':
        break
    print('-' * 22)
    print('  CADASTRE UMA PESSOA')
    print('-' * 22)

print(f'Total de pessoas com mais de 18 anos: {quant_idade}')
print(f'Ao todo temos {quant_homem} homens cadastrados')
print(f'E temos {mulher_menorDe20} mulheres com menos de 20 anos')