print('-='*8)
print('\033[31mMéDIA DO ALUNO\033[m')
print('-='*8)

nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
media = (nota2 + nota1) / 2
if media < 5:
    print(f'Com a média {media} você está \033[31mREPROVADO\033[m')
elif 7 > media >= 5:
    print(f'COm média {media} você está de \033[33mRECUPERAÇÃO!\033[m')
else:
    print(f'Com média de {media} você foi \033[36mAPROVADO!\033[m')