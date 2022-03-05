n = int(input('Digite um número: '))
c = n
f = 1
for cont in range(c, 0, -1):
	print(cont, end = '')
	print( 'x' if cont > 1 else '=', end = '')
	f *= c
	c-= 1
print(f)
