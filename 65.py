print('=-='*7)
print('\033[33mMAIOR E MENOR VALORES\033[m')
print('=-='*7)
cont = maior = menor = soma = media = 0
perg = 'S'
while perg != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    perg = str(input('Quer continuar? [S / N]: ')).upper().strip()[0]
print(f'Você digitou {cont} números e a média foi {soma/cont:.2f}')
print(f'O maior {maior} menor {menor}')