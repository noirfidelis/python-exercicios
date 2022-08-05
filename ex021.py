#Tocando uma Música
import pygame #módulo para criar jogos
pygame.init() #iniciar o pygame
pygame.mixer.music.load('ex021.mp3') #carregar a música
pygame.mixer.music.play() #tocar a música
input() #após nova versão do python, é preciso utilizar esse comando
pygame.event.wait() #espera a música terminar, para finalizar o programa