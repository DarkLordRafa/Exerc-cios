primeiro_termo = int(input('Qual o primeiro termo? '))
razão = int(input('Qual a razão da sua PA? '))
print('')
c = 1
termo = primeiro_termo
total_termos = 0
mais_termos = 10
while mais_termos:
	total_termos += mais_termos
	while c <= total_termos:
		print(termo, end = '->')
		termo += razão
		c += 1
	print('\033[1;33mIntervalo\033[m')
	mais_termos = int(input('\nQuantos termos mais você quer? '))
	print('')
print(f'\nSua progressão foi finalizada com {total_termos} termos.')
