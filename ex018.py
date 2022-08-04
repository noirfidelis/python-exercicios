#Seno, Cosseno e Tangente
from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja:'))#precisa converter para radianos
r = radians(ang)
seno = sin(r)
cos = cos(r)
tan = tan(r)
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')
print(f'O ângulo de {ang} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tan:.2f}')