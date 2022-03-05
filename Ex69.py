l = '-' * 42
print(l)
print('Cadastro de pessoas\n')
homens = maior18 = mulheres20 = 0
while True:
	sexo = str(input('Sexo: ')).strip().upper()[0]
	if not sexo in 'MF':
		print('\nOpção inválida! Tente de novo\n')
		continue
	idade = int(input('Idade: '))
	if sexo == 'M':
		homens += 1
	if idade > 18:
		maior18 += 1
	if sexo == 'F' and idade < 20:
		mulheres20 += 1
	continuar = str(input('\nDeseja continuar? ')).strip().upper()[0]
	print ('')
	while not continuar in 'SN':
		print('Opção inválida! Tente de novo\n')
		continuar = str(input('Deseja continuar? ')).strip().upper()[0]
		print('')
	if continuar == 'N':
		break
print(l)
print(f'Ao todo foram cadastrados {homens} homens, {maior18} pessoas são maiores de 18 anos, e {mulheres20} mulheres são menores de 20 anos.')
print(l)
