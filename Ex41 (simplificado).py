from datetime import date
nasc = int(input('Em que ano o atleta nasceu? '))
atual = date.today().year
idade = atual - nasc
print(f'\nO atleta tem {idade} anos.')

if idade <= 9:
	print('Categoria: Mirim')
elif idade <= 14:
	print('Categoria: Infantil')
elif idade <= 19:
	print('Categoria: Junior')
elif idade <= 25:
	print('Categoria: Sênior')
elif idade > 25:
	print('Categoria: Master')
