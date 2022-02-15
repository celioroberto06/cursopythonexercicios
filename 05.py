from time import sleep
n = int(input('Digite um número: '))
print(f'Analizando o valor {n}...')
sleep(1)
ant = n - 1
suc = n +1
print(f'O antecessor de {n} é {ant}\ne seu sucessor é {suc}')