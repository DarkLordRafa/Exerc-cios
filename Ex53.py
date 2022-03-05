frase = str(input('Digite sua frase: ')).strip().upper()
separado = frase.split()
junto = ''. join(separado)
inverso = ''

'''De uma forma mais simples usando
posicionamento de trás pra frente:'''

#inverso = junto[:: -1]

for contador in range(len(junto) - 1, -1, -1):
	inverso += junto[contador]
print(f'\nO inverso de {junto} é {inverso}\n')
if junto == inverso:
	print('Isso é um palíndromo!')
else:
	print('Não é um palíndromo.')
