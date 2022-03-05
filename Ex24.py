nome = str(input('Em que cidade você nasceu?: ')).upper().split()
print(f'O nome da cidade começa com "Santo?":\n{nome[0] == "SANTO"}')
