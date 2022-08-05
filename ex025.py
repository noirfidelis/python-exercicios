#Procurando uma string dentro de outra
nome = str(input('Qual é seu nome completo?')).upper().split()
print('Seu nome tem Silva?', 'SILVA' in nome)