print('-'* 23)
print('\033[:31mCONVERTENDO TEMPERATURA\033[m')
print('-'* 23)
temp = float(input('Qual a temperatura °C: '))
f = (temp * 1.8) + 32
print(f'A temperatura de {temp:.0f}° celsius e equivalete há {f:.0f}° em fahrenheit')