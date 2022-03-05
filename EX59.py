from time import sleep
l = '=' * 30
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = num1 + num2
mult = num1 * num2
opção = 0
print('')
while opção != 5:
	print(l)
	print('Escolha uma das opções:\n(1) Somar\n(2) Multiplicar\n(3) Maior\n(4) Novos Números\n(5) Sair do programa\n')
	opção = int(input('---> '))
	print('')
	if opção == 1:
		print(f'A soma de {num1} + {num2} é {soma}')
	elif opção == 2:
		print(f'A multiplicação de {num1} x {num2} é {mult}')
	elif opção == 3:
		if num1 > num2:
			print(f'O número maior é {num1}')
		elif num2 > num1:
			print(f'O número maior é {num2}')
		elif num1 == num2:
			print('Os números são iguais.')
	elif opção == 4:
		num1 = int(input('Digite o primeiro número: '))
		num2 = int(input('Digite o segundo número: '))
		soma = num1 + num2
		mult = num1 * num2
	elif opção == 5:
		print('\033[1;33mFinalizando programa...\033[m')
		sleep(3)
		print('')
		print('*' * 25)
		print('\033[1;34mPrograma finalizado\033[m')
		print('*' * 25)
	else:
		print('Opção inválida! Tente de novo')
