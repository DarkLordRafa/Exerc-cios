#Programa funcionando com erro para números menores:

#n = input('Digite um número: ')
#print(f'Unidade: {n[3]}\nDezena: {n[2]}\nCentena: {n[1]}\nMilhar: {n[0]}')

#Programa funcionando usando matemática para corrigir o problema

n = int(input('Digite um número: '))
print(f'Unidade: {n // 1 % 10}\nDezena: {n// 10 % 10}\nCentena: {n // 100 % 10}\nMilhar: {n // 1000 % 10}')
