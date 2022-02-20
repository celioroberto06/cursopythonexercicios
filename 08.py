# conversor de medidas

def linha(msg):
    print('-'*35)
    print(msg)
    print('-'*35)
linha('     CONVERSOR DE MEDIDAS')
valor = float(input('Digite um valor em metros: '))
cm = valor * 100
mm = valor * 1000
km = valor * 1000
hc = valor * 100
dc = valor * 10
dec = valor /10

print(f'{valor} em metros e equivalente à: ')
print(f'Cm - {cm:>10}')
print(f'mm - {mm:>10}')
print(f'km - {km:>10}')
print(f'hc - {hc:>10}')
print(f'dc - {dc:>10}')
print(f'dec - {dec:>10}')