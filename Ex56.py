velho = 0
mais_velho = ''
totmulher20 = 0
quantidade = 0
idade_m = 0
for p in range(1,5):
	nome = str(input('Digite o nome: '))
	idade = int(input('Idade: '))
	idade_m += idade
	quantidade += 1
	sexo = str(input('Sexo (M/F): ')).upper()
	print('')
	if p == 1 and sexo in 'Mm':
		velho = idade
		mais_velho = nome
	else:
		if sexo in 'Mm' and idade > velho:
			velho = idade
			mais_velho = nome
	if sexo in 'Ff' and idade < 20:
		totmulher20 += 1
média = idade_m / quantidade
print(f'A média de idade desse grupo de pessoas é {média:.1f}')
print(f'O homem mais velho tem {velho} amos e se chama {mais_velho}.')
print(f'O total de mulheres com menos de 20 anos foi de {totmulher20}.')
