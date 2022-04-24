from random import randint
print('PAR OU ÍMPAR')
print('=-'*9)
print('Vamos jogar par ou ímpar')
resultado = cont = v = 0
while True:
    computador = randint(1, 5)
    valor = int(input('Digite um valor: '))
    soma = computador + valor
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P / I] ')).upper().strip()[0]
    if soma % 2 == 0:
            resultado = 'Par'
    else:
        resultado = 'impar'
    print(f'O computador jogou {computador} e você {valor} total  {soma} deu {resultado}')
    print('=-' *20)
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Computador ganhou')
    if escolha == 'I':
        if soma % 2 != 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Computador venceu')
    cont += 1
    if cont == 3:
        break
print(f'GAMER OVER! Você venceu {v} vezes')