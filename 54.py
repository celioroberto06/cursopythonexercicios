from datetime import date
menor = maior = idade = 0
for c in range(1, 8):
    ano_nasc = int(input(f'Ano de nascimento da {c}º pessoa? '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if idade <= 18:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {maior} maiores de idade.')
print(f'E ao todo tivemos {menor} menores de idade.')