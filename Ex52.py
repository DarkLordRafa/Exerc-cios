total = 0
n = int(input('Digite um número: '))
print('')
for primo in range(1, n +1):
	if n % primo == 0:
		total += 1
		print(f'\033[1;32m{primo}\033[m', end = ' ')
	else:
		print(f'\033[1;31m{primo}\033[m', end = ' ')
if total == 2:
	print(f'\n\nO número {n} foi divisível 2 vezes. E por isso, É UM NÚMERO PRIMO.')
else:
	print(f'\n\nO número {n} foi divisível {total} vezes. E por isso, NÃO É UM NÚMERO PRIMO.')
