#Sorteando um item na lista
import random
al1 = input('Primeiro aluno:')
al2 = input('Segundo aluno:')
al3 = input('Terceiro aluno:')
al4 = input('Quarto aluno:')
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)#comando para sortear algo
print(f'O aluno escolhido foi {escolhido}')