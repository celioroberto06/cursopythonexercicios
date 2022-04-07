print('-='*10)
print('\033[1;36mEMPRéSTIMO BANCáRIO\033[m')
print('-='*10)
valor_casa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o sálario atual R$: '))
dividir = int(input('Números de parcelas: '))
parcelas = valor_casa / dividir
divisao_salario = salario * 30 / 100
if parcelas <= divisao_salario:
    print(f'Empréstimo APROVADO')
    print(f'Empréstimo de  {valor_casa:.2f} em  {dividir} vezes de {parcelas:.2f}')
else:
    print(f'\033[31mNEGADO!!!\033[m Infelizmente o valor da casa R$ {valor_casa:.2f} a parcela não pode ser menor que {parcelas:.2f}'.replace('.',','))