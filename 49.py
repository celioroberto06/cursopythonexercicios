print('-='*11)
print('\033[36mTABUADA\033[m')
print('-='*11)

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num*c}')