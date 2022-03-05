print('Vamos analisar 3 números e verificar qual é o maior.')
n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))
maior = n1
if n2 > n1 and n2 > n3:
	maior = n2
if n3 > n1 and n3 > n2:
	maior = n3
menor = n1
if n2 < n1 and n2 < n3:
	menor = n2
if n3 < n1 and n3 < n2:
	menor = n3
if n1 == n2 and n1 == n3:
	print('Os números são iguais!')
	exit()
print(f'O maior número é {maior}\nE o menor número é {menor}')
