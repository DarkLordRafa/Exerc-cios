from random import randint
numcpu = randint(0, 10)
print('''Olá, eu sou o computador. Estou pensando em um número entre 0 e 10. Tente adivinhar qual é!''')
acertou = False
tentativas = 0
while not acertou:
	numplayer = int(input('---> '))
	tentativas += 1
	if numplayer == numcpu:
		acertou = True
	else:
		if numplayer > numcpu:
			print('Pensei em um número menor. Tente de novo!')
		elif numplayer < numcpu:
			print('Pensei em um número maior. Tente de novo!')
print(f'Parabéns! Você acertou com {tentativas} tentativas.')
