#Analisador de Textos
import time
nome = str(input('Digite seu nome completo, por gentileza:')).strip()
print('Analisando seu nome...')
time.sleep(3) #comando para fazer a máquina esperar
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minísculas é {nome.lower()}')
print(f'Seu nome tem ao todo', len(nome.replace(' ','')), 'letras')
dividir = nome.split()
print(f'Seu primeiro nome é {dividir[0]} e ele tem', len(dividir[0]), 'letras')