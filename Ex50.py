soma = 0
vezes = 0
for p in range(1, 7):
	s = 'primeiro segundo terceiro quarto quinto sexto'. split()
	s = s[p - 1]
#Da pra fazer tudo de uma vez também na mesma variável:
	#s = 'primeiro segundo terceiro quarto quinto sexto'. split()[p - 1]
	n = int(input(f'Digite o {s} valor: '))
	if n % 2 == 0:
		soma += n
		vezes += 1
if vezes == 1:
	print(f'\nA soma de {vezes} valor par é igual a {soma}.')
else:
	print(f'\nA soma de {vezes} valores pares é igual a {soma}.')
