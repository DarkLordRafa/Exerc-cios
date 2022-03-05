nome = str(input('Digite um nome: ')).strip()
print (f'\nNome em maiúsculo:\n{nome.upper()}')
print(f'Nome em minúsculo:\n{nome.lower()}')
m = sum(1 for elem in nome if elem.isupper())
m2 = sum(1 for elem in nome if elem.islower())
print(f'Letras maiúsculas: {m}')
print(f'Letras minúsculas: {m2}')
print(f'Seu nome tem ao todo {len(nome)} letras.')
#Usando método replace para eliminar espaços:
#quantidade = len(nome.replace(' ', ''))
#print(f'Quantidade total de letras: {quantidade}')
#Forma mais simples de contar as letras da primeira palavra:
divi = nome.split()
print(f'Seu primeiro nome é {divi[0]} e ele tem {nome.find(" ")} letras.')
#Outra forma:
#divi = nome.split()
#print(f'Seu primeiro nome é {divi[0]} e ele possui {len(divi[0])} letras.')
