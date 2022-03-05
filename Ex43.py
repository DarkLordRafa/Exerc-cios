print('''Vamos calcular seu IMC (Índice de massa corpórea) de acordo com a Organização Mundial de Saúde?
Para fazer isso, basta informar abaixo a sua altura e o seu peso.
''')
alt = float(input('Altura (m): '))
pe = float(input('Peso (Kg): '))
imc = pe / (alt ** 2)
if imc < 18.5:
	condição = 'MAGREZA!'
elif 18.5 <= imc < 25 :
	condição = 'NORMAL.'
elif 25 <= imc < 30:
	condição = 'SOBREPESO.'
elif 30 <= imc < 40:
	condição = 'OBESIDADE.'
elif imc >= 40:
	condição = 'OBESIDADE MÓRBIDA, CUIDADO!'
print(f'Seu IMC é de {imc:.1f} e sua condição é: {condição}')
