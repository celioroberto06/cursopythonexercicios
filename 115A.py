lista = list()
cadastro = 0
while True:
      print('-'*30)
      print('MENU PRINCIPAL')
      print('-'*30)
      print('1 - Ver pessoas cadastradas\n'
            '2 - Cadastrar nova pessoa\n'
            '3 - Sair do sistema')
      print('-'*30)
      op = int(input('Sua opção: '))
      if op == '1':
            print('lista')
      elif op == '2':
            cadastro = str(input('nome:'))
      else:
            break
            print('Obrigado por usar o programa.')
