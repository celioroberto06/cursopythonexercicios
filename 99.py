from time import sleep


def maior (* núm):
    cont = maior = 0
    print('Analizando os valores passados...')
    print('-=' * 23)
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1


    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado fou {maior}.')
#programa príncipal
maior(2, 9, 4, 5, 7, 1)
maior(2, 5, 8,10)
maior(5, 6, 8 , 6, 9, 2)