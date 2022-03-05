valores  = soma = 0
while True:
	valor = int(input('Digite um valor (999 para parar): '))
	if valor == 999:
		break
	soma += valor
	valores += 1
print(f'\nVocê digitou {valores} valores e a soma entre eles foi {soma}')
