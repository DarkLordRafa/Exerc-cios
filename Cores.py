cores = {'limpa' : '\033[m', 
                'tpre' : '\033[7;30m',
                'tver' : '\033[1;31;47m',
                'tazu' : '\033[1;34;47m'}
                
print(f'O número 5 é {cores["tver"]}vermelho{cores["limpa"]} e o número 7 é {cores["tazu"]}azul{cores["limpa"]}.')
