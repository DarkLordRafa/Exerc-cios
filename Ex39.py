from datetime import date
print('''O alistamento militar é obrigatório para pessoas do sexo masculino a partir dos 18 anos de idade, e esta é a idade mínima para se alistar.''')
sexo = int(input('''
Qual seu sexo?

(1) Masculino
(2) Feminino

---> '''))
if sexo == 2:
	print('\nSeu alistamento não é obrigatório.\nDeseja continuar mesmo assim?\n\n(1) Sim\n(2) Não\n')
	cont = int(input('---> '))
	if cont == 2:
		exit()
nasc = int(input('\nInforme seu ano de nascimento.\n\n---> '))
print('')
ano_atual = date.today().year
idade = int(ano_atual) - int(nasc)
if idade == 18:
	print(f'Você tem {idade} anos.\nEstá na hora de se alistar!')
elif idade > 18:
	print(f'Você tem {idade} anos.\nSeu alistamento está atrasado em {idade - 18} anos.\nVocê deveria ter se alistado em {int(nasc) + 18}!')
else:
	print(f'Você ainda é muito jovem para se alistar!\nVocê tem apenas {idade} anos.\nAinda falta {18 - idade} anos para você se alistar.\nVocê poderá se alistar em {nasc + 18}!')
