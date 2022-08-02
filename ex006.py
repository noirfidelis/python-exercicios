#Dobro, Triplo e Raíz Quadrada
n = int(input('Digite um número:'))
d = n * 2
print(f'O dobro de {n} vale {d}')
t = n * 3
print(f'O triplo de {n} vale {t}')
r = n ** (1/2) #comando para calcular raíz quadrada
print(f'A raíz quadrada de {n} é igual a {r:.2f}') #:.1f (uma casa depois da vúrgula), :.2f (duas casas... etc)