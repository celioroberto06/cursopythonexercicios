print('-='*14)
print('\033[36mSE FORMA UM TRIâNGULO OU NÃO\033[m')
print('-='*14)

p1 = int(input('Primeiro seguimento: '))
p2 = int(input('Segundo seguimento: '))
p3 = int(input('Terceiro seguimento: '))

if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    if p1 == p2 == p3:
        print('Forma um triângulo EQUILÁTERO')
    elif p1 != p2 != p3 != p1:
        print('Forma um triângulo ESCALENO')
    else:
        print('Forma um triângulo ESÓSCELES')
else:
    print('\033[31mNÃO\033[m forma um triângulo ')