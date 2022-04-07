print('-='*10)
print('\033[1;36mCONVERSOR DE NúMEROS\033[m')
print('-='*10)

numero = int(input('Digite um número: '))
print('''Digite qual das opções você quer coverter:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O número {numero} convertido para Binário fica {bin(numero)[2:]}')
elif opcao == 2:
    print(f'O número {numero} convertido para binário fica {oct(numero)[2:]}')
elif opcao == 3:
    print(f'O número {numero} convertido para hexadecimal fica {hex(numero)[2:]}')