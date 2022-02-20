#Calcular a aréa pra saber quanto de tinta vai usar-
larg = float(input('Largura da parede: '))
comp = float(input('Comprimento da parede: '))
area = larg * comp
tinta = area / 2
print(f'Sua parede de {larg} x {comp} tem {area} m²')
print(f'Você vai precisar de {tinta:.2f}L de tintas para pintar toda parede')