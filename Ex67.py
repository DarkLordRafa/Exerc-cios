while True:
	valor = int(input('Você quer ver a tabuada de qual valor? '))
	print('')
	if valor < 0:
		break
	for contador in range(1, 11):
		tabuada = valor * contador
		#poderia usar apenas um print, com tudo na mesma linha, mas também da pra fazer usando o end
		print(f'{valor} x {contador} = ', end = '')
		print(f'{tabuada}')
	if contador == 10:
		print('')
