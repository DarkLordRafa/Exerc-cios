s = float(input('Qual o seu salário? R$: '))
if s <= 1250:
	a = s + (s * 15 / 100)
else:
	a = s + (s * 10 / 100)
print(f'O seu salário que era de R$ {s:.2f} agora passará a ser de R$ {a:.2f}.')
