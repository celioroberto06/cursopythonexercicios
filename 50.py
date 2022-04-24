print('-='*11)
print('\033[36mSOMANDO OS PARES\033[m')
print('-='*11)
soma = cont = 0
for c in range (1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A soma de todos os {cont} pares é {soma}')