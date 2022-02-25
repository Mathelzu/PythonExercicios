import math
angulo = float(input('Digite o ângulo que deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem: \nO seno de {sen:.2f} \nO cosseno de {cos:.2f} \nE a tangente de {tan:.2f}')