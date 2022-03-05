def nota1():
	n = float(input('Primeira nota: '))
	return n

def nota2():
	n = float(input('Segunda nota: '))
	return n
	
def calculo(n1, n2):
	m = (n1 + n2) / 2
	print('\nNota 1:', n1)
	print('Nota 2:', n2)
	print('Média:', m, '\n\nResultado: ', end = '\n')
	if m >= 7:
		print('Aprovado')
	else:
		print('Reprovado')

a = nota1()
b = nota2()
calculo(a, b)
