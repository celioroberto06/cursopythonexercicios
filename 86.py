matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0,3):
        matriz[c].append(int(input(f'Digite o valor {l, c}: ')))

print('='*30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()