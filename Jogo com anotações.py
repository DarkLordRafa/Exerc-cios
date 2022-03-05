#Comecei o programa importando as bibliotecas que eu iria utilizar:

from time import sleep
from random import randint, choice

#Texto de apresentação do jogo:

print('''Olá, eu sou o computador 😎
Vamos ver se você consegue ganhar de mim no famoso jogo Jokenpô. Ou pedra, papel, tesoura, se preferir.
Mas primeiro, vamos escolher seu avatar!
''')

#Primeiro loop com While para forçar o usuário a digitar uma das opcões:
#A primeira vez que coloquei emojis em um programa, usei os códigos unicode de emoji do Python, o que deu um baita trabalho, pois tinha que ficar procurando os códigos de cada um e digitando um por um, porém depois eu soube que o Python aceita os emojis do teclado mesmo, não precisa ficar colocando código, isso facilitou demais:

while True:
	avatar = input('(1)🙂 (2)😷 (3)👻 (4)💀 (5)👨 (6)👩 (7)🦖\n\n(8)🎃\n\n---> ')
	if avatar.isdecimal():
		avatar = int(avatar)
	else:
		print('\nOpção inválida!\nTente de novo\n')
		continue
	if not 0 < int(avatar) < 9:
		print('\nOpção inválida!\nTente de novo\n')
		continue
		
#break pra parar o loop do avatar:
		
	break

#Criei a variável *player* pra receber um dos emojis abaixo de acordo com o número de posicionamento que o usuário digitar no input da variável *avatar* menos 1, já que pro Python, a primeira posição é zero:

player = '🙂' '😷' '👻' '💀' '👨' '👩' '🦖' '🎃'[avatar - 1]
cpu = '😎'

#as novas versões do Python trouxeram o f string. É bem melhor do que usar o .format pra formatar os textos. Estude f string, vale a pena

print(f'\nSeu avatar: {player}')
print(f'\nAgora sim, vamos começar nosso joguinho. Prepare-se para perder 😎\nE quando você perder... SUA \033[1;31mALMA\033[m SERÁ MINHA\n{"😈":^40}\n\nQuer dizer... sua *\033[1;34mADMIRAÇÃO\033[m* será minha\n\n{"😎":^40}')
print('Vamos começar!')

#Mais um loop, agora para forçar o usuário a digitar uma das opções entre as 3 disponíveis: Pedra, papel, ou tesoura:

while True:
	cpu_choose = randint(1, 3)
	player_choose = input('\nEscolha uma das opções abaixo:\n\n(1) 🤜 (Pedra)\n(2) 🤚 (Papel)\n(3) ✌️ (Tesoura)\n\n---> ')
	if player_choose.isdecimal():
		player_choose = int(player_choose)
		
#Caso o usuário, ao invés de digitar uma das opções, digitar o nome MATRIX, criei um laço aninhado, um loop dentro desse loop das escolhas, para ficar printando as letras na cor verde aleatóriamente e infinitamente, pois não coloquei break nesse loop aninhado:
		
	elif player_choose == 'MATRIX':
		while True:
			print('\033[0;33m', choice('A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'X' 'W' 'Y' 'Z' '1' '2' '3' '4' '5' '6' '7' '8' '9'), end = '')
			
#Esse else abaixo é do laço das escolhas, não do laço aninhado, percebe-ce pela quantidade de espaços antes dele, que é chamado de identação. A identação é extremamente importante no Python quando usamos condições e loops. A identação deve estar perfeita para que o programa funcione corretamente, então preste atenção nos espaços, nenhum a mais nenhum a menos:
			
	else:
		print('\nPor favor escolha uma das opções!')
		continue
	if not  0< int(player_choose) < 4:
			print('\nPor favor escolha uma das opções!')
			continue
			
#Caso tudo acima esteja correto, o programa segue em frente, porém sem sair do loop das escolhas, pois ainda quero utilizá-lo mais pra frente:
			
	else:
		print('\n\033[1;33mCARREGANDO...\033[m\n')
		
#Essa função sleep é só pra dar um efeito legal de carregamento, mas é pura estética:
		
		sleep(2)
		
#As variáveis abaixo vão receber os seguintes emojis de acordo com o número da posição que o usúrio escolher lá em cima. A mesma coisa que fiz com a escolha de avatar:
		
		player_emoji = '🤜' '🤚' '✌️'[player_choose - 1]
		cpu_emoji = '🤜' '🤚' '✌️'[cpu_choose - 1]
		
#Aqui a variável *vencedor* vai receber o emoji de player ou cpu, de acordo com as condições abaixo:
		
	if player_choose == 1 and cpu_choose == 2:
		vencedor = cpu
	elif player_choose == 1 and cpu_choose == 3:
		vencedor = player
	elif player_choose == 2 and cpu_choose == 1:
		vencedor = player
	elif player_choose == 2 and cpu_choose == 3:
		vencedor = cpu
	elif player_choose == 3 and cpu_choose == 1:
		vencedor = cpu
	elif player_choose == 3 and cpu_choose == 2:
		vencedor = player
		
#Se nenhuma dessas condições acontecer, só resta o empate, e com isso podemos finalmente usar o else. E esse else, além de printar essas mensagens, vai gerar um outro loop dentro desse loop das escolhas. Esse segundo loop é para forçar o usuário a escolher se ele quer continuar ou não:
		
	else:
		print('Você   Computador')
		print(f'\n{player_emoji}    \033[1;31mVS\033[m   {cpu_emoji}\n\nEMPATOU 😎\nVamos de novo! 😎')
		while True:
			continuar = input('\n(1) Pode apostar!\n(2) Não\n\n---> ')
			if continuar.isdecimal():
				continuar = int(continuar)
			else:
				print('\nEscolha uma opção!')
				continue
			if 0 < int(continuar) < 3:
				break
			else:
				print('\nOpção inválida!\nTente de novo')
				continue
				
#Esses if e else abaixo estão dentro do loop das escolhas, não do loop do continuar, mais uma vez observe a quantidade de espaços:
				
		if continuar == 1:
			continue
		else:
			print('\n\nCOVARDE! 👿')
			
#Se o usuário optar por não continuar quando der empate e digitar 2, a função exit() vai encerrar o programa e finalizar por aqui mesmo:
			
			exit()
			
#Se tudo acima estiver correto, o laço das escolhas que está lá em cima bem longe, finalmente recebe um break:
			
	break
	
#E agora podemos finalmente printar os resultados na tela, de acordo com quem ganhou, o player ou a cpu:
	
print('Você   Computador')
print(f'\n{player_emoji}    \033[1;31mVS\033[m   {cpu_emoji}')
input(('\nPróximo --->'))

if vencedor == cpu:
	print(f'\nEU VENCI {cpu}')
	sleep(2)
	print(f'\nAgora sua \033[1;31mALMA\033[m é MINHA!\n\n              😈 HAHAHAHA!')
	sleep(4)
	print(f'''
             🏛️🏛️🏛️🏛️🏛️🏛️🏛️
             🏛️ ☆      ♂ 🏛️
             🏛️    😈    🏛️
             🏛️          🏛️
             🏛️    {player}    🏛️
             🏛 ♀      † 🏛️
             🏛️🏛️🏛️🏛️🏛️🏛️🏛️''')

elif vencedor == player:
	print(f'\nEU VENCI {player}')
	sleep(2)
	print(f'\nO que? Eu PERDI? 🤨')
	input('\nPróximo --->')
	print('\nIsso não é possível 👿')
	input('\nPróximo --->')
	print('\nNão posso perder para um HUMANO! 👿')
	input('\nPróximo --->')
	print('...')
	sleep(3)
	print('''               NÃÃÃÃÃÃÃÃO!!!
	     🔥🔥🔥🔥🔥🔥🔥
             🔥💥💥💥💥💥🔥
             🔥💥💥💥💥💥🔥
             🔥💥💥👿💥💥🔥
             🔥💥💥💥💥💥🔥
             🔥💥💥💥💥💥🔥
             🔥🔥🔥🔥🔥🔥🔥

Você venceu o computador e salvou sua alma
...''')
if vencedor == player:
	sleep(4)
	input('\nPróximo --->')
	print('\nParece que o computador deixou cair algo\n...')
	sleep(4)
	print('\nÉ um pedaço de papel velho\n...')
	sleep(4)
	input('\nPróximo --->')
	print('\n"MATRIX"')
	sleep(4)
