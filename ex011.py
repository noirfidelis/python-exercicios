#Pintando Parede
larg = float(input('Largura da Parede:'))
alt = float(input('Altura da Parede:'))
print(f'Sua parede tem a dimensão de {larg}X{alt}. Sua área é de {larg * alt}m².')
print(f'Para pintar essa parede, você precisará de {(larg * alt) / 2}l de tinta.')