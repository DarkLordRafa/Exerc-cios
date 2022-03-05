from datetime import date
a = int(input('Qual ano você quer analisar? Digite 0 se quiser analisar o ano atual: '))
if a == 0:
	a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
	print(f'O ano de {a} é um ano bissexto!')
else:
	print(f'O ano de {a} não é um ano bissexto.')
