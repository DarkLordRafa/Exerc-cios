total = mais1000 = menor = 0
l = '=-' * 21
l2 = '-' * 42
print(f'             Loja Night Tech\n{l}\n')
while True:
	nome = str(input('Nome do produto: '))
	preço = float(input('Preço (R$): '))
	total += preço
#Forma tradicional:
#	if menor == 0:
#		menor = preço
#		maisbarato = nome
#	if preço < menor:
#		menor = preço
#		maisbarato = nome

#Forma simplificada:
	if menor == 0 or preço < menor:
		menor = preço
		maisbarato = nome
	if preço > 1000:
		mais1000 += 1
	while True:
		continuar = str(input('\nComprar mais? (S/N): ')).strip().upper()[0]
		print('')
		if not continuar in 'SN':
			print('Opção inválida! Tente de novo')
			continue
		if continuar in 'SN':
			break
	if continuar == 'N':
		break
print(l)
print('')
print(l2)
print(f'O total da compra foi de R$ {total:.2f}\n{mais1000} produtos custaram mais de R$ 1000\nE o produto mais barato foi {maisbarato}, custando R$ {menor:.2f}')
print(l2)
