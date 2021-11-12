from datetime import date
atual = date.today().year
print(f'Ano atual: {atual}')
informados = 0
anulados = 0
pessoas_maioridade = 0
pessoas_jovens = 0
print('\nDigite o ano de nascimento de uma pessoa.\n(0 para anular)\n')
for c in range(1, 8):
	ordem = 'Primeiro Segundo Terceiro Quarto Quinto Sexto Sétimo'.split()
	ordem = ordem[c - 1]
	nascimento = int(input(f'{ordem} indivíduo\nAno: '))
	if nascimento == 0:
		anulados += 1
		print('')
	else:
		informados += 1
		idade = atual - nascimento
		print(f'Idade: {idade}\n')
		if idade >= 21:
			pessoas_maioridade += 1
		else:
			pessoas_jovens += 1
if informados == 1 and pessoas_maioridade == 1:
	print('Somente uma pessoa informou o ano de nascimento, e essa pessoa atingiu a maioridade.')
elif informados == 1 and pessoas_maioridade == 0:
	print('Somente uma pessoa informou o ano de nascimento, e essa pessoa ainda não atingiu a maioridade.')
elif informados > 1 and pessoas_maioridade == 1:
	print(f'{informados} pessoas informaram o ano de nascimento, e apenas uma delas atingiu a maioridade.')
elif informados > 1 and pessoas_maioridade == 0:
	print(f'{informados} pessoas informaram o ano de nascimento.\nNenhuma delas atingiu a maioridade.')
#Usando pass:
elif informados == 0:
	pass
else:
	print(f'{informados} pessoas informaram o ano de nascimento.\nDessas {informados} pessoas, {pessoas_maioridade} atingiram a maioridade, e {pessoas_jovens} ainda não atingiram.')
if anulados == 1:
	print(f'\nUma pessoa preferiu não informar o ano de nascimento.')
elif 7 > anulados > 1:
	print(f'\n{anulados} pessoas preferiram não informar o ano de nascimento.')
elif anulados == 7:
	print('Nenhuma pessoa forneceu o ano de nascimento.')

'''Se não quiser usar o pass, basta criar uma condição aninhada, o método tradicional.
A variável *anulados*  receber ela mesma é opcional nesse caso:

elif informados == 0:
	anulados = anulados
	if anulados == 1:
		print(f'\nUma pessoa preferiu não informar o ano de nascimento.')
	elif 7 > anulados > 1:
		print(f'\n{anulados} pessoas preferiram não informar o ano de nascimento.')
	elif anulados == 7:
		print('Nenhuma pessoa forneceu o ano de nascimento.')
else:
	print(f'{informados} pessoas informaram o ano de nascimento.\nDessas {informados} pessoas, {pessoas_maioridade} atingiram a maioridade, e {pessoas_jovens} ainda não atingiram.')'''
