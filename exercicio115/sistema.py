from exercicio115.lib.interface import *
from exercicio115.lib.arquivo import *
from time import sleep

#manipulação de dados-


arq = 'curso em video.txt'

if not arquivoExiste(arq):
   criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Programa' ])
    if resposta == 1:
        #opção de mostrar o conteúdo do arquivo
        lerArquivo(arq)
        #print(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa-
        cabeçalho('NOVO CADASTRO')
        nome =str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
        sleep(1)
