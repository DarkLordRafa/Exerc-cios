maior = 0
menor = 0
for c in range(1, 6):
	ordem = 'primeiro segundo terceiro quarto quinto'.split()[c - 1]
	peso = float(input(f'Informe o {ordem} peso (Kg): '))
	if c == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso
print(f'\nO maior peso lido foi {maior:.1f}\nE o menor peso lido foi {menor:.1f}')
