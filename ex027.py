#Primeiro e último nome de uma pessoa
nome = str(input('Digite seu nome completo:')).strip()
print('Muito prazer em te conhecer!')
separa = nome.split()
print('Seu primeiro nome é', separa[0])
print('Seu último nome é', separa[-1])