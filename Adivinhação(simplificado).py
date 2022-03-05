import time
import random
l = '=' * 24
cn = random.randint(0, 5)
print('\nBem-vindo!\nEu sou o computador 😎\n\nAntes de começar-mos nosso joguinho, escolha seu avatar:\n\n(1)👨 (2)😷 (3)🦇 (4)🤺 (5)😈\n')

while True:
	avatar = input('----> ')
	if avatar.isdecimal():
		avatar = int(avatar)
	else:
		print('Escolha uma das opções acima!')
		continue
	if not  0 < int(avatar) < 6:
		print('Escolha uma das opções acima!')
		continue
	else:
		break

player = '👨😷🦇🤺😈'[avatar - 1]
print(f'\nAvatar: {player}')
print('\n\033[0;33mCARREGANDO...\033[m\n')
time.sleep(3)
print('\033[37;44mTente adivinhar o número (entre 0 e 5) que o computador está pensando.\033[m')

while True:
	un = input('\nDigite um número: ')
	if not un.isdecimal():
		continue
	if not -1 < int(un) < 6 :
		print('O número deve ser entre 0 e 5!')
		continue
	print('\n\n\033[0;33mCARREGANDO...\033[m\n\n')
	time.sleep(2)
	if int(cn) == int(un):
		print(f'\033[1;37;44mParabéns!\033[m\n\nO número era realmente {cn}\n\nVocê venceu\n\n{l}\n|  \033[1;33;44mWINNER\033[m  {player}   \033[1;33;44mWINNER\033[m  |\n{l}')
	else:
		print(f'\033[1;37;41mErrado!\033[m\n\nO número era {cn}!\n\nO computador venceu\n\n\n{l}\n|  \033[1;33;44mWINNER\033[m  😎   \033[1;33;44mWINNER\033[m  |\n{l}\n\n')
	break
