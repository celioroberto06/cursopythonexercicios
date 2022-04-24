while True:
    perg = str(input('Informe o sexo [M / F]')).upper().strip()[0]
    if perg in 'MF':
        print(f'Sexo {perg} registrado com sucesso.')
        break
    else:
        print('Resposta inválida, tente novamente!')