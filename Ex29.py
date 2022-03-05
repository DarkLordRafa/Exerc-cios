v = int(input('Qual a velocidade em que o carro estava?(km/h): '))
if v > 80 :
	print(f'Você excedeu o limite de velocidade e por isso foi multado no valor de R$ {(v - 80) * 7}.')
