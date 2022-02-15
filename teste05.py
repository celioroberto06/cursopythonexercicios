import outcome

lista = []

lista.append(str(input('nome: ')))
lista.append(int(input('Idade: ')))

for i in lista:
    for v in outcome.Values():
        print(v)