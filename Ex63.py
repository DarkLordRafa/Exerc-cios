l1 = '-' * 42
l2 = '=' * 42
print(l1)
print('          Sequência de Fibonacci')
print(l1)
print('')
print(l2)
termos = int(input('Quantos termos você quer ver?: '))
print('')
termo1 = 0
termo2 = 1
print(f'{termo1}-> {termo2}', end = '-> ')
contador = 3
while contador <= termos:
	próximo_termo = termo1 + termo2
	termo1 = termo2
	termo2 = próximo_termo
	print(próximo_termo, end = '-> ')
	contador += 1
print('FIM')
print(l2)