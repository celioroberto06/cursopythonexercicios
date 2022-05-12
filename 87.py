totPar = total = maior= maior_coluna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))

print('='*30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            totPar += matriz[l][c]
    print()

for l in range(0, 3):
    maior_coluna += matriz[l][2]

for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]

print('='*30)

print(f'A soma de todos os valores pares é {totPar}')
print(f'A soma da terceira colula é {maior_coluna}')
print(f'O maior valor da segunda linha é {maior}')