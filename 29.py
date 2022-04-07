print('-='*10)
print('MEDIDOR DE VELOCIDADE')
print('-='*10)
sua_velocidade = float(input('Digite a velocidade que você estava: '))
multa = (sua_velocidade - 80) * 7
velocidade_acima = sua_velocidade - 80
if sua_velocidade > 80:
    print(f'Limite de velocidade é de 80km\n'
          f'Você passou há {velocidade_acima}km acima do permitido\n')
    print(f'E pagará uma multa de {multa:.2f}'.replace('.',','))
else:
    print(f'Limite de velocidade é de 80km\n'
          f'E você está dentro dele.')