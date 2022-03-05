acumulador = 0
contador = 0
for t in range(1, 501, 2):
	if t % 3 == 0:
		acumulador  += t
		contador += 1
print(f'A soma de todos os {contador} valores é igual a {acumulador}')
