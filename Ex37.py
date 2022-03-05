num = int(input('Digite um número inteiro: '))
c = int(input('''Digite uma das opções abaixo para converter o número:
[1] Converter para binário
[2] Converter para Octal
[3] Converter para Hexadecimal

---> '''))
if c == 1:
	print(f'O número {num} convertido para binário é {bin(num)[2:]}')
elif c == 2:
	print(f'O número {num} convertido para octal é {oct(num)[2:]}')
elif c == 3:
	print(f'O número {num} convertido para hexadecimal é {hex(num)[2:]}')
else:
	print('''\033[1;31mOpção inválida!\033[m
Tente novamente''')
