cont = soma = 0
while True:
    valor = int(input('Digite um valor [999 PARA PARAR]: '))
    if valor == 999:
        break
    cont += 1
    soma += valor

print(f'ao totatl foram digitados {cont} números e a soma entre eles são {soma}')