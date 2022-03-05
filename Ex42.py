def amarelo():
	print('\033[1;33m')
	return ''

def vermelho():
	print('\n033[1;31m')
	return ''
	
def fim():
	print('\033[m')
	return ''

print('Vamos analisar o comprimento de 3 retas (em cm) e calcular se é possível que elas formem um triângulo!\n')
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a != b and b != c and c != a:
	tipo = 'ESCALENO'
elif a == b and a != c or b == c and b != a or c == a and c != b:
	tipo = 'ISÓSCELES'
elif a == b and b == c and c == a:
	tipo = 'EQUILÁTERO'
if a + b > c and a + c > b and b + c > a:
	print(f'Essas retas \033[1;33mPODEM\033[m formar um triângulo {tipo}.')
else:
	print('Essas retas \033[1;31mNÃO PODEM\033[m formar um triângulo!')
