from random import randint
l = '-' * 42
l2 = '=-' * 21
vitórias = 0
print('Tente vencer o computador no jogo de par ou ímpar.\nSe você perder, o jogo acaba.')
while True:
	print('')
	jogador_escolha = str(input('Você escolhe par ou ímpar? (P/I) ')).upper()
	if jogador_escolha != 'P' and jogador_escolha != 'I':
		print('Opção Inválida, tente de novo!')
		continue
	jogador_número = int(input('Digite um número de 0 a 10: '))
	print('')
	computador_número = randint(0, 10)
	soma = jogador_número + computador_número
	if soma % 2 == 0:
		resultado = 'PAR'
		resultado2 = 'P'
	else:
		resultado = 'ÍMPAR'
		resultado2 = 'I'
	if resultado2 == jogador_escolha:
		vitórias += 1
		print(l)
		print(f'Você = {jogador_número}\nComputador = {computador_número}\nSoma = {soma} \nResultado = {resultado}\nVocê acertou! Vamos continuar...')
		print(l)
	else:
		print(l)
		print(f'Você = {jogador_número}\nComputador = {computador_número}\nSoma = {soma}\nResultado = {resultado}\nVocê perdeu!')
		print(l)
		break
if vitórias > 0:
	print('')
	print(l2)
if vitórias == 1:
	print('Você venceu apenas uma vez.')
if 1 < vitórias <= 4:
	print(f'Você venceu {vitórias} vezes seguidas!')
elif 4 < vitórias <= 9:
	print(f'Você venceu {vitórias} vezes seguidas!\nVocê é demais! 😁')
elif vitórias >= 10:
	print(f'Você venceu {vitórias} vezes seguidas!\nVocê é um monstro! 😎')
if vitórias > 0:
	print(l2)
