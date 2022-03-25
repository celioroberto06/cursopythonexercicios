frase = str(input('Digite uma frase: ')).upper().strip()
quantidade = len(frase)
letra = frase.count('A')
apareceu = frase.find('A') + 1
ultima = frase.rfind('A') + 1

print(f'A letra A apareceu {letra} vezes\n'
      f'A primeira vez que aparece a letra A é na posição {apareceu}\n'
      f'A ultima vez que aparece a letra A é na posição {ultima}')
