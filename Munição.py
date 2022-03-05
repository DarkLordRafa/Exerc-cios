import random
ammo =int('10')
print(f'Munição [{ammo}]')
rint = random.randint(3, 10)
print(f'Você achou Munição de Pistola({rint})\nPegar munição?\n(1)Sim\n(2)Não')
takeammo = input()
if takeammo == '1' :
	print(f'\nMunição[{ammo + rint}]\n')
else:
	print('Você devolve o item')
print('(1)Seguir em frente\n(2)Continuar explorando')
c1 = str(input())
if c1 == '1' :
	print('Você segue o caminho')
else:
	print('Você continua no local')
	