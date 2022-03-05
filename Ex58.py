from random import randint
tentativas = 1
numcpu = randint(0, 10)
print('Olá, eu sou o computador 😎')
numplayer = int(input('''
Tente adivinhar o número que eu estou pensando (de 0 a 10).
---> '''))
while not -1 < numplayer < 11:
	print('\nO número deve ser entre 0 e 10!')
	numplayer = int(input('---> '))
while not numplayer == numcpu:
	if numplayer < numcpu:
		print('\nPensei em um número \033[1;31mmaior\033[m. Tente de novo.')
		tentativas += 1
		numplayer = int(input('---> '))
	elif numplayer > numcpu:
		print('\nPensei em um número \033[1;33mmenor\033[m. Tente de novo.')
		tentativas += 1
		numplayer = int(input('---> '))
if tentativas == 1:
	print('\nVocê acertou de primeira 😦. Será que você tem poderes?')
else:
	print(f'\nVocê acertou! Com {tentativas} tentativas.')
