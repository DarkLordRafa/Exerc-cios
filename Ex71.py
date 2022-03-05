l = '-' *42
print(f'{"Caixa eletrônico":^42}')
print(l)
valor = int(input('Quanto deseja sacar? R$ '))
total = valor
cédulas = 50
totcédulas = 0
print('')
while True:
	if total >= cédulas:
		total -= cédulas
		totcédulas += 1
	else:
		if totcédulas > 0:
			print(f'Cédulas de {cédulas}: {totcédulas}')
		if cédulas == 50:
			cédulas = 20
		elif cédulas == 20:
			cédulas = 10
		elif cédulas == 10:
			cédulas = 1
		totcédulas = 0
		if total == 0:
			break
print(l)
