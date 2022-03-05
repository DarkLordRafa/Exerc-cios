import math
an = float(input('Informe o ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(f'O ângulo de {an}° possui Seno de {sen:.2f}, Cosseno de {cos:.2f} e Tangente de {tan:.2f}. ')
