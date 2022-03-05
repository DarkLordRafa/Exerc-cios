print('Vamos analisar 3 números e verificar qual é o maior.')
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))
if n1 > n2 and n1 > n3:
	print(f'O maior número é o número {n1}!')
if n2 > n1 and n2 > n3:
	print(f'O maior número é o número {n2}!')
if n3 > n1 and n3 > n2:
	print(f'O maior número é o número {n3}!')
if n1 == n2 and n1 == n3:
	print('Os números são iguais!')
if n1 < n2 and n1 < n3:
	print(f'E o menor número é o número {n1}!')
if n2 < n1 and n2 < n3:
	print(f'E o menor número é o número {n2}!')
if n3 < n1 and n3 < n2:
	print(f'E o menor número é o número {n3}!')
