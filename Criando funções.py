def nota1():
	n = float(input('Primeira nota: '))
	return n

def nota2():
	n = float(input('Segunda nota: '))
	return n

def calculo(n1, n2):
	m = (n1 + n2) / 2
	print(f'\nNota 1: {n1}')
	print(f'Nota 2: {n2}\n')
	if m >= 7:
		print(f'Média {m:.1f}!\n\nParabéns! Você passou.')
	else:
		print(f'Média {m:.1f}!\n\nVocê foi reprovado.\nTente de novo no próximo ano.')

a = nota1()
b = nota2()
calculo(a, b)
