elementos = []
expressao = str(input('Digite a expressão: '))
for simb in expressao:
    if simb == '(':
        elementos.append('(')
    elif simb == ')':
        if len(elementos) > 0:
            elementos.pop()
        else:
            elementos.append(')')
            break
if len(elementos) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada! ')