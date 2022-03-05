ptermo = int(input('Digite o primeiro termo da sua P.A.: '))
razão = int(input('Digite a razão da sua P.A.: '))
c = 1
termo = ptermo
while c <= 10:
	print(termo, end = '->')
	termo += razão
	c += 1
print('FIM')
