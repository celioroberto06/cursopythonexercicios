print('='*19)
print('\033[31mNúMEROS PRIMOS\033[m')
print('='*19)
tot = 0
num = int(input('Digite um número: '))

for c in range (1, num +1):
   if num % c == 0:
      tot += 1
      print('\033[36m', end='')
   else:
      print('\033[31m', end='')
   print(f'{c}', end=' ')
print(f'\033[m\nO número {num} foi divisível {tot} vezes')
if tot == 2:
   print('E por isso ele é PRIMO')
else:
   print('E por isso ele não é PRIMO')