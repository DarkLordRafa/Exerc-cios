while True:
	número = int(input('Digite um número entre 0 e 20: '))
	if not 0 <= número <= 20:
		print('\nO número deve ser entre 0 e 20!\n')
		continue
	extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')[número]
	print(f'\nO número digitado foi {extenso}.')
	while True:
		continuar = str(input('\nDeseja continuar? (S/N): ')).strip().upper()[0]
		if continuar in 'SN':
			break
		else:
			print('\nOpção inválida! Tente de novo')
			continue
	if continuar == 'S':
		print('')
	elif continuar == 'N':
		break
