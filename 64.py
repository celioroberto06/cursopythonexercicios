print('=-='*8)
print('\033[33mTRATANDO VáRIOS VALORES\033[m')
print('=-='*8)
valor = soma= cont =0
while valor != 999:
    valor = int(input('Digite um número [999 para parar]: '))
    if valor != 999:
        soma += valor
        cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')