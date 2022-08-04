#carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
total = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R$ {total:.2f}')