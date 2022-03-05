print('''Você está andando por uma estrada quando se depara com uma bifurcação de 3 direções.
Você possui consigo 3 itens...
Um pote de mel
Uma espada
E uma pena''')
input('\nPróximo --->')
print('''
No caminho da esquerda, há um urso faminto e furioso
No caminho do centro, há um dragão feroz
No caminho da direita, há um poderoso gigante''')
input('\nPróximo --->')
print('''
Qual você escolhe?

(1) Caminho da esquerda
(2) Caminho do centro
(3) Caminho da direita''')
choose = int(input('\n---> '))
if choose == 1:
	print('''
Você joga o pote de mel ao chão, esperando que o urso se distraia com a comida e assim lhe dê uma brecha para passar.
Pro seu azar o urso ignora completamente o mel e avança em sua direção.
Você é rasgado em pedaços pelo urso e morre em gritos de agonia.''')
elif choose == 2:
	print('''
Você fica cara a cara com a majestosa criatura, e com uma grande bravura e arrogância, saca sua espada para acabar com o inimigo.
Porém, com um simples gesto, o dragão o abocanha e arranca sua cabeça fora.
Você morre sem nem mesmo ter tido chance de lutar.''')
elif choose == 3:
	print('''
Você oferece o mel para o gigante, que fica muito contente e o deixa passar de bom grado.''')
	input('\nMoral da história --->')
	print('\nUm gesto de bondade, gera outro.')
