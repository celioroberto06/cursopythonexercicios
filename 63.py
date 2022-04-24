print('=-='*6)
print('\033[31mSEQUêNCIA FIBONACCI\033[m')
print('=-='*6)
cont = 1
num = int(input('Quantos termos você quer ver? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(f' -> {t3}',end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' fim')