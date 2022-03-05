L = '=' * 15
print(L, 'Dark Store', L)
compras = float(input('\nValor da compra (R$): '))
while True:
	pagamento = (input('\nEscolha a forma de pagamento:\n\n[1] À vista no dinheiro/cheque\n[2] À vista no cartão\n[3] No cartão em 2x\n[4] No cartão em 3x ou mais\n\n---> '))
	print('')
	desconto10 = (compras * 10) / 100
	desconto5 = (compras * 5) / 100
	juros = (compras * 20) / 100
	if  pagamento.isdecimal():
		pagamento = int(pagamento)
	else:
		print('Escolha uma das opções acima!')
		continue
	if not 0 < int(pagamento) < 5:
		print('Escolha uma das opções acima!')
		continue
	if pagamento == 1:
		print(f'Sua compra de R$ {compras} obteve desconto.\nVocê pagará R$ {compras - desconto10:.2f}')
	elif pagamento == 2:
		   print(f'Sua compra de R$ {compras} obteve desconto.\nVocê pagará R$ {compras - desconto5:.2f}')
	elif pagamento == 3:
		   	parcelamento = 2
		   	print(f'Sua compra de R$ {compras} será parcela em 2 vezes de R$ {compras / parcelamento:.2f}\nSem alteração no preço final.')
	elif pagamento == 4:
		  while True:
		  	parcelamento = input('\nQuantas parcelas? ')
		  	if parcelamento.isdecimal():
		  		parcelamento = int(parcelamento)
		  		print('')
		  		print(f'Sua compra de R$ {compras:.2f} será parcelada em {parcelamento} vezes de R$ {compras / parcelamento:.2f} com juros.\nVocê pagará no total R$ {compras + juros:.2f}')
		  		break
		  	else:
		  		print('\nValor inválido!\nTente novamente.')
		  		continue
	break