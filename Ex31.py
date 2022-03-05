d = float(input('Qual a distância que você deseja viajar? (km/h): '))
if d <= 200:
	print(f'A viagem ficará no valor de R$ {0.50 * d:.2f}.')
else:
	print(f'A viagem ficará no valor de R$ {0.45 * d:.2f}.')
	