valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c}º valor na posição {c}: ')))
print('='*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições: ', end=' ')
for pos, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{pos+1}...',end=' ')
print(f'\nO menor valor digitado foi {min(valores)} na posição: ',end=' ')
for pos, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{pos+1}...',end=' ')