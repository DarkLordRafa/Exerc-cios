from time import sleep
n = int(input('Digite um número: '))
contador = n
f = 1
print(f'\nCalculando {n}!')
sleep(2)
while contador > 0:
	print(f'{contador}', end = '')
	print('x' if contador > 1 else '=' , end = '')
	f *= contador
	contador -= 1
print(f)
