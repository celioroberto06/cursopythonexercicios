import random

nomes = []
cont = sorteio = 0
for c in range(4):
    cont+=1
    nomes.append(str(input(f'Digite o nome do {cont}º aluno: ')))
random.shuffle(nomes)
print(f'A orde de apresentação é:\n{nomes}')
