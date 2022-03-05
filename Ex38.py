print('''Digite dois números para compará-los!''')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if n1 > n2:
	print('\nO primeiro número é maior.')
elif n2 > n1:
	print('\nO segundo número é maior.')
else:
	print('\n\033[1;32mOs números são iguais!\033[m')
	