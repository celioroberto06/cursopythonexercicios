nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
primeiro_nome = separa[0]
ultimo_nome = separa[-1]
print(f'Olá {nome}')
print(f'Seu primeiro nome é {primeiro_nome} e o ultimo é {ultimo_nome}')