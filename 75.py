n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
n4 = int(input('Digite o 4º número: '))
valores = (n1, n2, n3, n4)
print(f'O valor 9 apraceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}º posição')
else:
    print(f'O valor 3 nao foi digitado em nenhuma posição!')
print('Os valores pares digitados foram: ',end='')
for num in valores:
    if num % 2 == 0:
        print(num, end=' ')