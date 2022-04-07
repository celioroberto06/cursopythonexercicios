lado1 = lado2 = lado3 = 0

print('-='*13)
print('\033[1;32mANALIZADOR DE TRIâNGULOS\033[m')
print('-='*13)
lado1 = float(input('Primeiro seguimento: '))
lado2 = float(input('Segundo seguimento: '))
lado3 = float(input('Terceiro seguimento: '))


if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('FORMA um triângulo')
else:
    print('\033[31mNÃO\033[m forma um triângulo ')