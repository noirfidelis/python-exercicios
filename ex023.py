#Separando dígitos de um número
import time
n = int(input('Informe um número:'))
print(f'Analisando o número {n}...')
time.sleep(3)
uni = n // 1 % 10 # // ---> divisão inteira  % ---> resto da divisão
print(f'Unidade: {uni}')
dez = n // 10 % 10 #O "10" é para pegar apenas 1 digíto. "100" 2 digítos etc...
print(f'Dezena: {dez}')
cent = n // 100 % 10
print(f'Centena: {cent}')
mil = n // 1000 % 10
print(f'Milhar: {mil}')