casa = float(input('Qual o valor da casa que deseja comprar?\n----> R$ '))
salário = float(input('Qual o seu salário?\n----> R$ '))
anos = int(input('Em quantos anos pretende pagar?\n----> '))
meses = anos * 12
parcelas = casa / meses

if casa >= 200000:
	print('\n\033[0;30;46mVocê está comprando uma casa cara!\033[m💲🏡💲😮\n')
if parcelas <= (salário * 30) / 100:
	print(f'A prestação da casa que você está comprando no valor de R$ {casa:.2f}, parcelado em {anos} anos, será de R$ {parcelas:.2f}.\n\033[1;32mFINANCIAMENTO CONCEDIDO\033[m')
elif parcelas > (salário * 30) / 100:
	print(f'\nVocê não pode comprar esta casa, pois o valor da prestação (R$ {parcelas:.2f}) excede 30% do seu salário.\n\033[1;31mFINANCIAMENTO NEGADO!\033[m')
