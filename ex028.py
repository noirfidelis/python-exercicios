#Jogo da Adivinhação v.1.0
import random
import time
computador = random.randint(0, 5) #comando para o computador sortear um número entre 0 e 5
print('\033[1;33m-=-\033[m' * 20)
print('\033[1;34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[1;33m-=-\033[m' * 20)
jogador = int(input('\033[97mEm que número eu pensei?\033[m')) #jogador tenta adivinhar
print('\033[1;35mProcessando...\033[m')
time.sleep(3)
if computador == jogador:
    print('\033[1;31mImpossível...\033[m') # primeiros sinais da skynet
else:
    print(f'\033[1;32mVENCI! Eu pensei no {computador} e não no {jogador}!\033[m')