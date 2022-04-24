totImpar = contImpar = 0

for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        contImpar += 1
       # print(contImpar, end=' ')
        totImpar += c
print(f'A soma de todos os {contImpar} números ímpares é {totImpar}')