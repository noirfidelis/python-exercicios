#Custo da Viagem
# R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = float(input('R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas. Digite aqui:'))
if dist <= 200:
    preço = 0.50 * dist
    print(f'Você está prestes a começar uma viagem de {dist:.2f} Km')
    print(f'E o preço da sua passagem será de R$ {preço:.2f}')
else:
    desconto = 0.45 * dist
    print(f'Você está prestes a começar uma viagem de {dist:.2f} Km')
    print(f'E o preço da sua passagem será de R$ {desconto:.2f}')