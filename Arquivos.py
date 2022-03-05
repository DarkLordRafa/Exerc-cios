file = open('Texto.txt', 'w')
file.write(input('Escreva no arquivo: '))
file.close()

file = open('Texto.txt', 'r')
print(file.read())
file.close()
