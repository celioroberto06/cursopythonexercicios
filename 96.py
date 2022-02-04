#Medidor de área

def área(larg, comp):
    s = larg * comp
    print(f'A área do seu terreno de {comp} x {larg} tem  {s}m².')


print('Controle de terrenos')
print('=-'*11)
c = float(input('Comprimento do terreno: '))
l = float(input('Largura do terreno: '))
área(l, c)
