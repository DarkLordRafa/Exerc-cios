sexo = str(input('Digite seu sexo (M para masculino, ou F para feminino: ')).strip().upper()[0]
while not sexo in 'MF':
	print('\nInformação incorreta!\nTente novamente.\n')
	sexo = str(input('Digite seu sexo (M para masculino, ou F para feminino: ')).strip().upper()
if sexo == 'M':
	print(f'\nO sexo informado foi MASCULINO.')
elif sexo == 'F':
	print('\nO sexo informado foi FEMININO.')
