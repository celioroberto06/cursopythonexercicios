print('TABUADA COM WHILE')
print('=-'*9)
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    for c in range (1, 11):
        print(f'{num} x {c} = {num*c}')
    print('=-' * 19)
    if num < 0:
        break