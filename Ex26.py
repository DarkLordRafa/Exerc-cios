frase = str(input('Digite algo: ')).upper().strip()
#Para contar também as letras com til:
#frase = frase.replace('Ã' , 'A')
print(f'Na frase "{frase.capitalize()}", a letra "a" aparece {frase.count("A")} vezes.\nA letra "a" aparece pela primeira vez na posição {frase.find("A") + 1}.')
print(f'E aparece pela última vez na posição {frase.rfind("A") + 1}.')
