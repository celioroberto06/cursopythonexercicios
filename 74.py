from random import randint
maior = menor = cont = 0
numero = ('1', '2', '3', '4','5','6','7','8','9','10')
n = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))
print(f'Os valores sortedos foram {n}')
for c in n:
    cont += 1
    if cont == 1:
        maior = menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c

print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
print('='*25)


# outro jeito
from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')

print('='*25)
# outro jeito
numero = ('1', '2', '3', '4','5','6','7','8','9','10')
n = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))
print(f'Os valores sortedos foram {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
