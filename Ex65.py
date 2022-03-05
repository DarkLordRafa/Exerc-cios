continuar = 'S'
soma = quantidade = 0
while not continuar in 'Nn':
	n = int(input('Digite um número: '))
	soma += n
	quantidade += 1
	if quantidade == 1:
		maior = menor = n
	if n > maior:
		maior = n
	if n < menor:
		menor = n
	continuar = str(input('\nDeseja continuar? ')).strip()[0]
	print('')
if maior != menor:
	print(f'\nVocê digitou {quantidade} números e a média foi {soma / quantidade:.2f}\nO maior número foi {maior} e o menor número foi {menor}')
else:
	print(f'\nVocê digitou {quantidade} números e a média foi {soma / quantidade:.2f}\nOs números são iguais')
