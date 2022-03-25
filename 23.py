num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analizando o número {num}')
print(f'Unidade {u:3}')
print(f'Dezena {d:4}')
print(f'Centena {c:3}')
print(f'Milhar {m:4}')
