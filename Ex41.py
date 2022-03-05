from datetime import date
nasc = int(input('Em que ano o atleta nasceu? '))
atual = date.today().year
idade = atual - nasc
print(f'\nO atleta tem {idade} anos.')

if 10 > idade > -1:
	print('Categoria: Mirim')
elif 15 > idade > 9:
	print('Categoria: Infantil')
elif 20 > idade > 14:
	print('Categoria: Junior')
elif 26 > idade > 19:
	print('Categoria: Sênior')
elif idade > 25:
	print('Categoria: Master')
