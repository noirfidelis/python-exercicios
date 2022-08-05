#Primeira e última ocorrência de uma string
frase = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece', frase.count('A'), 'vezes na frase.')
print('A primeira letra A apareceu na posição', frase.find('A')+1)
print('A última letra A apareceu na posição', frase.rfind('A')+1)