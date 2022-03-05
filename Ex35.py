print('Vamos analisar o comprimento de 3 retas (em cm) e calcular se é possível que elas formem um triângulo!')
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a + b > c and b + c > a and a + c > b:
	print('Essas retas podem formar um triângulo.')
else:
	print('Essas retas não podem formar um triângulo!')
	