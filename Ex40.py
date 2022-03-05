def vermelho():
	print('\033[1;31m', end = '')
	return ''

def amarelo():
	print('\033[1;33m', end = '')
	return ''

def azul():
	print('\033[1;34m', end = '')
	return ''

def fim():
	print('\033[m', end = '')
	return ''

n1 = float(input(f'Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
	print(f'\nMédia: {m:.1f}')
	print(f'\n{vermelho()}REPROVADO'), fim()
elif m >= 5 and m < 7:
	print(f'\nMédia: {m:.1f}')
	print(f'\n{amarelo()}RECUPERAÇÃO!'), fim()
#Aqui pode usar elif ou else, tanto faz
elif m >= 7:
	print(f'\nMédia: {m:.1f}')
	print(f'\n{azul()}APROVADO\n\nPARABÉNS!'), fim()
	print('😁')
