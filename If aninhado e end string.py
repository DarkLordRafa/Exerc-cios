print('Vamos analisar o comprimento de 3 retas (em cm) e calcular se é possível que elas formem um triângulo!\n')
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a + b > c and a + c > b and b + c > a:
	print('\nEssas retas \033[1;33mPODEM\033[m formar um triângulo ', end = '')
	if a != b and b!= c and c != a:
		print('ESCALENO.')
#Forma clássica:
	#elif a == b and b == c:
#Simplificando com Python:
	elif a == b == c:
		print('EQUILÁTERO.')
	else:
		print('ISÓSCELES.')
else:
	print('\nEssas retas \033[1;31mNÃO PODEM\033[m formar um triângulo!')
